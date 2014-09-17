"""
View which can render and send email from a contact form.

"""

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.template import RequestContext
from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'

    def display_form(self,self.request):
        if self.request.method == 'POST':
            form = self.formclass(self.request.POST)
            if form.is_valid():
                self.form_valid()
        else:
            form= self.formclass(self.request)
        c={'form': self.formclass}
        return render_to_response(self.template_name, c,context_instance=RequestContext(self.request))

    def form_valid(self, form):
        
        form.save()

        return super(ContactFormView, self).form_valid(form)

    def get_form_kwargs(self):
        # ContactForm instances require instantiation with an
        # HttpRequest.
        kwargs = super(ContactFormView, self).get_form_kwargs()

        kwargs.update({'request': self.request})
       
        return kwargs

    def get_success_url(self):
        # This is in a method instead of the success_url attribute
        # because doing it as an attribute would involve a
        # module-level call to reverse(), creating a circular
        # dependency between the URLConf (which imports this module)
        # and this module (which would need to access the URLConf to
        # make the reverse() call).
        return reverse('contact_form_sent')

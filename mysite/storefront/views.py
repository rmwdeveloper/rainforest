from django.shortcuts import render , render_to_response , redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json
from django.core.validators import validate_email
from forms import ProductForm
# Create your views here.

def storefront_main(request):
	if request.method == "POST":
		pass
	else:
		if request.user.is_authenticated():
			form = ProductForm()
			return render_to_response('storefront.html', {'form': form, 'errors':form.errors}, context_instance = RequestContext(request))
			
		return HttpResponseRedirect('/login/')
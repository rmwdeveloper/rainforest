from django.shortcuts import render_to_response , redirect
from django import forms
from forms import UserCreateForm
from django.http import  HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from models import MyUserManager , UserProfile
import json

# Create your views here.

def landing(request):
    return render_to_response('landing.html', context_instance = RequestContext(request))

def register(request):
    if request.user.is_authenticated():
        
        return redirect('/')

    if request.method == 'POST':
        user_information = {
        'username': request.POST['username'],
        'password1': request.POST['password1'],
        'password2': request.POST['password2'],
        'last_name': request.POST['last_name'],
        'city': request.POST['city'],
        'first_name': request.POST['first_name'],
        'state': request.POST['state'],
        'middle_initial': request.POST['middle_initial'],
        'birth_date': request.POST['birth_date'],
        'email': request.POST['email'],
        'street_address': request.POST['street_address'],
        'zip_code': request.POST['zip_code']
        }

        form = UserCreateForm(user_information)
        if form.is_valid():
           
            form.save()
            return redirect('/') 
        else: 
            form_errors = form.errors
            return render_to_response('register.html', {'errors': form_errors, 'form': form}, context_instance=RequestContext(request))
    else: #AJAX form validation
        request_copy = request.GET.copy()
      

        if 'username' in request_copy: #Username in use?
            name = request_copy['username']
            response_data = {}
            if UserProfile.objects.filter(username__iexact=name): 
                response_data['result'] = 'false'
            else:           
                response_data['result'] = 'true'
            return HttpResponse(response_data['result'] , content_type = 'text/plain')
            # return HttpResponse(json.dumps(response_data), content_type = "application/json")
        if 'email' in request_copy: #Email in use?
            entered_email = request_copy['email']
            response_data = {}
            if UserProfile.objects.filter(email__iexact=entered_email):
                response_data['result'] = 'false'
            else:
               response_data['result'] = 'true'
            return HttpResponse(response_data['result'], content_type = 'text/plain')
        else:
            form = UserCreateForm()
            return render_to_response("register.html", {'form': form, 'errors':form.errors}, context_instance=RequestContext(request))
    
def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
         # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect('/')
            else:
                # An inactive account was used - no logging in!
                return redirect('/')
        else:
            # Bad login details were provided. So we can't log the user in.
            
            return redirect ('/')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('landing.html', {}, context)

@login_required
def user_logout(request):
    logout(request)

    return redirect('/')


from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext

def portfolio(request):
    return render_to_response('portfolio.html', context_instance = RequestContext(request))
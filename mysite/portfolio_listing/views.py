from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext
from models import Project

def portfolio(request):
	projects = Project.objects
	
	return render_to_response('portfolio.html',{'projects':projects}, context_instance = RequestContext(request))
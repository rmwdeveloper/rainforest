from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext
from models import Project

def construct_project_attribute_dictionary():
	"""
	Constructs a dictionary where the keys are project attribute type (frameworks..languages etc.)
	and value is an array of the attributes. 
	"""
	attribute_dictionary = { 'languages': [], 
							'frameworks': [],
							'cms': [],
							'databases': [],
							'concepts': [],
							}
	projects = Project.objects.all()

	for project in projects:
		for language in project.languages.all():
			if language not in attribute_dictionary['languages']:
				attribute_dictionary['languages'].append(language)

		for framework in project.frameworks.all():
			if framework not in attribute_dictionary['frameworks']:
				attribute_dictionary['frameworks'].append(framework)

		for content_management_system in project.cms.all():
			if content_management_system not in attribute_dictionary['cms']:
				attribute_dictionary['cms'].append(content_management_system)

		for database in project.databases.all():
			if database not in attribute_dictionary['databases']:
				attribute_dictionary['databases'].append(database)

		for concept in project.concepts.all():
			if concept not in attribute_dictionary['concepts']:
				attribute_dictionary['concepts'].append(concept)
	return attribute_dictionary



def portfolio(request):
	
	projects = Project.objects.all()
	attributes = construct_project_attribute_dictionary()
	return render_to_response('portfolio.html',{'projects':projects, 
												'languages':attributes['languages'],
												'frameworks':attributes['frameworks'],
												'cms': attributes['cms'],
												'databases': attributes['databases'],
												'concepts': attributes['concepts']}, context_instance = RequestContext(request))
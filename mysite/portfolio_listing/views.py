from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from models import Project , ProjectImage
import json

def construct_project_attribute_dictionary():
	"""
	Constructs a dictionary where the keys are project attribute type (frameworks..languages etc.)
	and value is an array of the attributes. This is so only those attributes that are part of actual 
	portfolio projects will  be <select> options in the template. 
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

def construct_project_image_dict():
	"""
	Constructs a dictionary where the keys are project id's and the values are
	arrays of ProjectImage image's.
	"""
	project_images = ProjectImage.objects.all()
	project_image_dict = {}

	for project_image in project_images:
		if project_image.project_id in project_image_dict:
			project_image_dict[project_image.project_id].append(project_image.image)
		else:
			project_image_dict[project_image.project_id] = []
			project_image_dict[project_image.project_id].append(project_image.image)

	return project_image_dict

def construct_projects_to_be_shown_array(form_data):
	"""
	Constructs an array of projects to be shown after a get request. Any project that doesn't have a selected technology
	in the form won't be shown. 
	Form data is data sent to the server, which is an array of technology names(eg mySQL, jQuery, Python etc.)
	"""

	projects = Project.objects.all()
	project_attribute_dict = {}
	projects_to_show = [] #Array of project ids. This will be the projects that will show after user filters them.

	# has_value returns bool dependending if arr_to_check has a val that's also in arr of vals
	has_value = lambda arr_to_check, arr_of_vals: bool(set(arr_to_check).intersection(arr_of_vals))

	for project in projects:
		project_attribute_dict[str(project.id)] = []
		projects_to_show.append(str(project.id))

		for language in project.languages.all():
				project_attribute_dict[str(project.id)].append(language.__unicode__())

		for framework in project.frameworks.all():
				project_attribute_dict[str(project.id)].append(framework.__unicode__())

		for content_management_system in project.cms.all():
				project_attribute_dict[str(project.id)].append(content_management_system.__unicode__())

		for database in project.databases.all():
				project_attribute_dict[str(project.id)].append(database.__unicode__())

		for concept in project.concepts.all():
				project_attribute_dict[project.id].append(concept.__unicode__())
	for project_id , attribute_array in project_attribute_dict.iteritems():
		if not has_value(attribute_array , form_data): 
			projects_to_show.remove(str(project_id))
	projects_to_show = [ int(project) for project in projects_to_show]
	
	return projects_to_show




def portfolio(request):
	
	projects = Project.objects.all()
	project_images = construct_project_image_dict()

	attributes = construct_project_attribute_dictionary()

	if 'form_inputs' in request.GET:

		jsonDecoder = json.JSONDecoder()
		jsonEncoder = json.JSONEncoder()
		form_input_array = jsonDecoder.decode(request.GET['form_inputs'])

		projects_to_show = jsonEncoder.encode(construct_projects_to_be_shown_array(form_input_array))
		return HttpResponse(projects_to_show)
		# return render_to_response('portfolio.html', context_instance = RequestContext(request))

	return render_to_response('portfolio.html',{'projects':projects,
												'project_images':project_images, 
												'languages':attributes['languages'],
												'frameworks':attributes['frameworks'],
												'cms': attributes['cms'],
												'databases': attributes['databases'],
												'concepts': attributes['concepts']}, context_instance = RequestContext(request))
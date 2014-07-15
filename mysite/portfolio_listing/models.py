from django.db import models

# Create your models here.
class Project(models.Model):
	"""
	Main table for a portfolio project.
	"""
	project_id = models.AutoField(primary_key=True)
	name = models.CharField()
	description = models.CharField()
	date_finished = models.Datefield()
	date_posted = models.DateTimeField()

class ProjectTypeValidation(models.model):
	"""Validation Table """
	project_type_id = models.AutoField(primary_key=True)
	name = models.CharField()
	description = models.CharField()
		

class ProjectType(models.Model):
	"""
	Linking table between Project and ProjectTypeValidation
	"""
	project_id = models.ForeignKey(Project)
	project_type_id = models.ForeignKey(ProjectTypeValidation)



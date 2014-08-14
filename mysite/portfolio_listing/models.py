from django.db import models

# Create your models here.


class Language(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __unicode__(self):
            return self.name
	
class Framework(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __unicode__(self):
            return self.name
class ContentManagementSystem(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __unicode__(self):
            return self.name
class Database(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __unicode__(self):
            return self.name
class Concept(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	def __unicode__(self):
            return self.name

def content_file_name(instance, filename):
    return '/'.join(['project_images/',instance.project.name, filename])

class Project(models.Model):
	"""
	Main table for a portfolio project.
	"""
	project_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	description = models.TextField()
	date_finished = models.DateField()
	date_posted = models.DateTimeField()
	languages = models.ManyToManyField(Language , blank=True)
	frameworks = models.ManyToManyField(Framework, blank=True)
	cms = models.ManyToManyField(ContentManagementSystem, blank=True)
	databases = models.ManyToManyField(Database, blank=True)
	concepts = models.ManyToManyField(Concept, blank=True)
	
	url = models.URLField()
	def __unicode__(self):
            return self.name

class ProjectImage(models.Model):
	project = models.ForeignKey(Project, related_name='images')
	image = models.ImageField(upload_to=content_file_name)


# class ProjectTypeValidation(models.Model):
# 	"""Validation Table """
# 	project_type_id = models.AutoField(primary_key=True)
# 	name = models.CharField()
# 	description = models.CharField()
		

# class ProjectType(models.Model):
# 	"""
# 	Linking table between Project and ProjectTypeValidation
# 	"""
# 	project_id = models.ForeignKey(Project)
# 	project_type_id = models.ForeignKey(ProjectTypeValidation)



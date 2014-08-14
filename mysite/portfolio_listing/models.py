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

class Project(models.Model):
	"""
	Main table for a portfolio project.
	"""
	project_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	description = models.TextField()
	date_finished = models.DateField()
	date_posted = models.DateTimeField()
	languages = models.ManyToManyField(Language)
	frameworks = models.ManyToManyField(Framework)
	cms = models.ManyToManyField(ContentManagementSystem)
	databases = models.ManyToManyField(Database)
	concepts = models.ManyToManyField(Concept)
	image = models.ImageField()
	url = models.URLField()



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



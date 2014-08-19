from django import forms
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from models import Project , ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


class ProjectAdmin(OrderedModelAdmin):
	inlines = [ ProjectImageInline, ]
	list_display = ('name', 'move_up_down_links')
	
admin.site.register(Project, ProjectAdmin)
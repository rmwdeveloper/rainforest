from django import template
import re
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name="placeholder")
def placeholder(value, token):
	value.field.widget.attrs["placeholder"] = token
	return value
 

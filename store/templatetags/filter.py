from django.template import Library

register = Library()

@register.filter
def where_id(models, find_id):
	return filter(lambda x:x.id==int(find_id), models)
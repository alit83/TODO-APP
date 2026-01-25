from django import template
from doing.models import Planer
register=template.Library()


@register.simple_tag(takes_context=True)
def task_count(context):
    request = context['request']
    return Planer.objects.filter(user=request.user , done=None).count()

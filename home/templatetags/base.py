from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db.models import Avg, Sum
from django import template
from testimony.models import  Testimony


register = template.Library()


# User=settings.AUTH_USER_MODEL

# @register.inclusion_tag('category/category_layouts/category.html')
# def job_panel():
#     infoForm=InformationForm()
#     return {
#                     'infos':infoForm,
#     }


@register.simple_tag(takes_context=True, name='user_count')
def user_count(context):
    request = context['request']
    print(context)
    users = User.objects.exclude(username='conic').count()
    return users


@register.simple_tag(takes_context=True, name='group_count')
def group_count(context):
    request = context['request']
    users = Group.objects.count()
    return users


@register.simple_tag(name='testimony_count')
def testimony_count():
    groups = Testimony.objects.count()
    return groups



@register.simple_tag(takes_context=True, name='groups_name')
def groups_name(context):
    request = context['request']
    for group in request.user.groups:
        return{
            'groups_name': groups_name
        }


# @register.simple_tag(name='total_amount', takes_context=True)
# def total_amount(context):
#     _t = Balance.objects.aggregate(total=Sum('total'))
#     return _t











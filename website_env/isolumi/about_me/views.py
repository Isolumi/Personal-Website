""" views.py"""

from django.http import HttpResponse
from django.template import loader

def about_me(request):
    template = loader.get_template('page.html')
    return HttpResponse(template.render())

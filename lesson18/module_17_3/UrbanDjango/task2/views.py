from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class class_template(TemplateView):
    template_name = 'class_template.html'

class func_template(TemplateView):
    template_name = 'func_template.html'

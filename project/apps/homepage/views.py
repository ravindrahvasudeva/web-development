from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class Ssview(TemplateView):
    template_name = 'homepage/homepage.html'
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import people

from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    products = people.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    return HttpResponse("we are here to help you")



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(response):
    return HttpResponse("Hello, welcome to the blog post app!")

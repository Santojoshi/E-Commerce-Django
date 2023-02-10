from django.http import HttpResponse
from django.shortcuts import render

def app1home(request):
    return HttpResponse('This is APP1 Home page ')

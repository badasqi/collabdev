from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Collab-Dev Zzzzzz</h1>')

def user(request):
    return HttpResponse('<h1>User</h1>')

def project(request):
    return HttpResponse('<h1>Project</h1>')
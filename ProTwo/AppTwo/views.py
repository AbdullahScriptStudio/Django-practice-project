from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'apptwo/help.html')

def about(request):
    return HttpResponse('about page')

def help(request):
    return render(request, 'apptwo/help.html')


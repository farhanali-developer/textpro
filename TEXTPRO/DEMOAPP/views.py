from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'DEMOAPP/index.html')

def file_system(request):
    return render(request,'DEMOAPP/file_system.html')

def signup(request):
    return render(request, 'DEMOAPP/signup.html')
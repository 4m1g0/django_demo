from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is our first view!")
    
def detail(request, id):
    return HttpResponse("This is the details page of gallery: " + str(id))

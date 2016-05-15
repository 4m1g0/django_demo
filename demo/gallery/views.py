from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

def index(request):
    galleries = Gallery.objects.all()
    html = ''
    for gallery in galleries:
        url = '/gallery/' + str(gallery.id) + '/'
        html += '<a href="' + url + '">' + gallery.name + '</a><br>'
        
    return HttpResponse(html)
    
def detail(request, id):
    return HttpResponse("This is the details page of gallery: " + str(id))

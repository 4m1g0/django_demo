from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery
from django.template import loader

#def index(request):
#    galleries = Gallery.objects.all()
#    html = ''
#    for gallery in galleries:
#        url = '/gallery/' + str(gallery.id) + '/'
#        html += '<a href="' + url + '">' + gallery.name + '</a><br>'
#        
#    return HttpResponse(html)

def index(request):
    galleries = Gallery.objects.all()
    template = loader.get_template('gallery/index.html')
    context = {
        'galleries' : galleries
    }
    
    return HttpResponse(template.render(context, request))
    

def detail(request, id):
    return HttpResponse("This is the details page of gallery: " + str(id))

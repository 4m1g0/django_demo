from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
from .models import Gallery
#from django.template import loader

#def index(request):
#    galleries = Gallery.objects.all()
#    html = ''
#    for gallery in galleries:
#        url = '/gallery/' + str(gallery.id) + '/'
#        html += '<a href="' + url + '">' + gallery.name + '</a><br>'
#        
#    return HttpResponse(html)

#def index(request):
#    galleries = Gallery.objects.all()
#    template = loader.get_template('gallery/index.html')
#    context = {
#        'galleries' : galleries
#    }
#    
#    return HttpResponse(template.render(context, request))

def index(request):
    galleries = Gallery.objects.all()
    context = {'galleries' : galleries}
    return render(request, 'gallery/index.html', context)
    

def detail(request, id):
    try:
        gallery = Gallery.objects.get(pk=id)
    except Gallery.DoesNotExist:
        raise Http404("This gallery does not exists")
    return render(request, 'gallery/details.html', {'gallery':gallery})

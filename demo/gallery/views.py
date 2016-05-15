from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404, HttpResponseBadRequest
from .models import Gallery
from django.views.generic import View
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

#def index(request):
#    galleries = Gallery.objects.all()
#    context = {'galleries' : galleries}
#    return render(request, 'gallery/index.html', context)

#def create(request):
#    try:
#        gallery = Gallery()
#        gallery.name = request.POST['name']
#        gallery.description = request.POST['description']
#        gallery.save()
#    except (KeyError):
#        return HttpResponseBadRequest("Error al recibir el formulario")
#        
#    return index(request)

class index(View):
    def get(self, request):
        galleries = Gallery.objects.all()
        context = {'galleries' : galleries}
        return render(request, 'gallery/index.html', context)
    
    def post(self, request):
        try:
            gallery = Gallery()
            gallery.name = request.POST['name']
            gallery.description = request.POST['description']
            gallery.save()
        except (KeyError):
            return HttpResponseBadRequest("Error al recibir el formulario")
            
        return self.get(request)

def detail(request, id):
    try:
        gallery = Gallery.objects.get(pk=id)
    except Gallery.DoesNotExist:
        raise Http404("This gallery does not exists")
    return render(request, 'gallery/details.html', {'gallery':gallery})

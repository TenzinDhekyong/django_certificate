from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

#importing get_template from loader
from django.template.loader import get_template

#import render_to_pdf from util.py 
from .utils import render_to_pdf 
# Create your views here.
def landing_view(request, *args, ** kargs):
    return render(request,"home.html",{})


def base_view(request, *args, **kargs):
    return render(request,"base_certi.html",{})

def eyrc(request, *args, **kargs):
    return render(request,"eyrc_certi.html",{} )

def eyic(request, *args, **kargs):
    return render(request,"eyic_certi.html",{} )

def event(request, *args, **kargs):
    return render(request,"event.html",{} )
def template(request, *args, **kargs):
    return render(request,"template.html",{} )
def generate(request, *args, **kargs):
    return render(request,"generate.html",{} )



#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('base_certi.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='certi/pdf')

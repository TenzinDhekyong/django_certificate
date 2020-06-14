from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django_tex.shortcuts import render_to_pdf
# #importing get_template from loader
# from django.template.loader import get_template

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


class GeneratePdf(View):       
    def get(self, request, *args, **kwargs):
        # data = {
             
        #      'amount': 39.99,
        #     'customer_name': 'Cooper Mann',
        #     'order_id': 1233434,
        # }
    
        # pdf = render_to_pdf('templates/base_certi.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')

        template_name = 'test.tex'
        context = {'foo': 'Bar'}
        return render_to_pdf(request, template_name, context, filename='test.pdf')
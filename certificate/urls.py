from django.contrib import admin
from django.urls import path
from  certificate.views import landing_view,base_view,eyrc,eyic,event,template,generate
from certificate.views import GeneratePdf
urlpatterns = [
    
    path('', landing_view, name ='landing'),
    path('base/', base_view, name='base'),
    path('eyrc/',eyrc, name='eyrc'),
    path('eyic/',eyic, name='eyic'),
   path('event/', event, name='event'),
   path('template/', template, name='template_certi'),
   path('generate/', generate, name='generate'),
   path('pdf/',GeneratePdf.as_view()),
]

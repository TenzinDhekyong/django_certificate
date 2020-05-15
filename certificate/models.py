from django.db import models

# Create your models here.
class Eyrc_certi(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    e_mail = models.EmailField(max_length=254,default='SOME STRING')
    generated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
from django.db import models

# Create your models here.
class Wsdl(models.Model):
    name = models.CharField(max_length=200)
    endpoint = models.TextField()

class Method(models.Model):
    wsdlId = models.ForeignKey('owscall.Wsdl')
    name = models.CharField(max_length=200)
    paremeters = models.TextField()

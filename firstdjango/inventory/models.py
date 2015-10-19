from django.db import models

class Item(models.Model):
    title= models.charField(max-lenght=200)
    description = models.TextField()
    amount = models.ImtegerField()

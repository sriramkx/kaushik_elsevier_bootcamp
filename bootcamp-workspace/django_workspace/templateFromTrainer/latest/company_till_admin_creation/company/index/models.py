from django.db import models

# Create your models here.

class about(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=300,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title

class pricingModel(models.Model):
    prodName = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    image=models.ImageField(upload_to='pricingProduct/', blank=False)
    def __str__(self):
        return self.prodName


class clientsModel(models.Model):
    clientName = models.CharField(max_length=100, blank=False)
    clientLink = models.CharField(max_length=300,blank=False)
    clientLogo=models.ImageField(upload_to='clientLogos/', blank=False)
    def __str__(self):
        return self.clientName
    

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=800, blank=False)    
    def __str__(self):
        return self.name
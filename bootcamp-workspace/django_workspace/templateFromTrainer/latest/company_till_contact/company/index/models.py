from django.db import models

# Create your models here.
class about(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=300,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title


class client(models.Model):
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=300,blank=False)
    image=models.ImageField(upload_to='client/',blank=False)

    def __str__(self):
        return self.name
   
class contactform(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.CharField(max_length=100,blank=False)
    subject=models.CharField(max_length=400,blank=False)
    message=models.TextField(max_length=800,blank=False)
    

    def __str__(self):
        return self.name
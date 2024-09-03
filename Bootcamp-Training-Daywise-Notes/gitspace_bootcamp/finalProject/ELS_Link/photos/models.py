from django.db import models

# Create your models here.

class photo(models.Model):
    image = models.ImageField(upload_to='photos/', blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

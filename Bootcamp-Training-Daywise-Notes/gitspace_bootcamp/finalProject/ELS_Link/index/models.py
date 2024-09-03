from django.db import models

# Create your models here.
class newsmodel(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=300,blank=False)
    image = models.ImageField(upload_to='newsmodel/',blank=False)

class postFeed(models.Model):
    postFeedId = models.AutoField(primary_key=True)
    postContent = models.TextField(max_length=500, blank=False)
    # imageUploaded = models.ImageField(upload_to='upload_images/', blank=False)

    def __str__(self):
        return self.postFeedId
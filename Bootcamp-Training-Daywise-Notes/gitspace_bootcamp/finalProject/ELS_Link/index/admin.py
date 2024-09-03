from django.contrib import admin

# Register your models here.
from .models import newsmodel
from .models import postFeed

admin.site.register(newsmodel)
admin.site.register(postFeed)
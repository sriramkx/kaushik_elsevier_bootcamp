from django.contrib import admin

# Register your models here.


from .models import contactlist
from .models import contactform



admin.site.register(contactlist)
admin.site.register(contactform)
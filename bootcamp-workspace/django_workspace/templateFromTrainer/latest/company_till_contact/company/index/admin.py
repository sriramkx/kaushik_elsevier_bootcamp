from django.contrib import admin

# Register your models here.
from .models import about
from .models import client
from .models import contactform

admin.site.register(about)

admin.site.register(client)
admin.site.register(contactform)
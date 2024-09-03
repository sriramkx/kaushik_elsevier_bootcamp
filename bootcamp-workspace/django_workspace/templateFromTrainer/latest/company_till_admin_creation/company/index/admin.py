from django.contrib import admin

# Register your models here.
from .models import about
from .models import pricingModel
from .models import clientsModel
from .models import contactform


admin.site.register(about)
admin.site.register(pricingModel)
admin.site.register(clientsModel)
admin.site.register(contactform)
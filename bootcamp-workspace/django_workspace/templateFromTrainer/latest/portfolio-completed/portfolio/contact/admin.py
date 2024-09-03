import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import contactlist
from .models import contactform

# Register your models here.

@admin.action(description='Export selected items to CSV')
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'

    writer = csv.writer(response)

    fields = [field.name for field in modeladmin.model._meta.fields]
    writer.writerow(fields)

    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])

    return response

class YourModelAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

 

admin.site.register(contactlist, YourModelAdmin)
admin.site.register(contactform)
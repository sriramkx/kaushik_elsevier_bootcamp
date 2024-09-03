import csv
from django.http import HttpResponse
from django.contrib import admin

# Register your models here.


from .models import about
from .models import slider
from .models import client
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .resources import YourModelResource


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

# class YourModelAdmin(admin.ModelAdmin):
#     actions = [export_as_csv]

class YourModelAdmin(ImportExportModelAdmin):
    resource_class = YourModelResource


admin.site.register(about)
admin.site.register(slider)
admin.site.register(client, YourModelAdmin)


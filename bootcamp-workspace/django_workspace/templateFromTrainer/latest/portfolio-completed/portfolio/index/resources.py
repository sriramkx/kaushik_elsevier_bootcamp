from import_export import resources
from .models import client

class YourModelResource(resources.ModelResource):
    class Meta:
        model = client
        fields = ('id', 'name', 'link', 'image')
 

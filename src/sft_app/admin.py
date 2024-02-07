from django.contrib import admin

# Register your models here.
from .models import Application, Contract, Manufacturer, Product

admin.site.register(Application)
admin.site.register(Contract)
admin.site.register(Manufacturer)
admin.site.register(Product)

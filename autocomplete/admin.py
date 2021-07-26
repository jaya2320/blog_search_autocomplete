from django.contrib import admin
from .models import CarBrand
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(CarBrand,CarAdmin)
from django.contrib import admin
from .models import Tour
# Register your models here.

class TourAdmin(admin.ModelAdmin):
    list_display = [f'{field.name}' for field in Tour._meta.fields]

admin.site.register(Tour, TourAdmin)

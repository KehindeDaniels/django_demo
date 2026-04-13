from django.contrib import admin
from .models import Tour
# Register your models here.

class TourAdmin(admin.ModelAdmin):
    # for each filed in the Tour model, return a list of field names
    list_display = [field.name for field in Tour._meta.fields]

admin.site.register(Tour, TourAdmin)

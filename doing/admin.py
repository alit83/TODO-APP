from django.contrib import admin
from .models import Planer
# Register your models here.
class PlanerAdmin(admin.ModelAdmin):
    list_display=['task','user']

admin.site.register(Planer,PlanerAdmin)
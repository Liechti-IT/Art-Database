from django.contrib import admin
from .models import Record

class imageAdmin(admin.ModelAdmin):
    list_display = ["img_title", "img"]

admin.site.register(Record, imageAdmin)
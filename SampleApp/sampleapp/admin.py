"""
Administration for sampleapp
"""

from .models import MyObject
from django.contrib.admin import ModelAdmin, site


class MyObjectAdmin(ModelAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')

site.register(MyObject, MyObjectAdmin)

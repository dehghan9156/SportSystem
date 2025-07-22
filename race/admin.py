from django.contrib import admin
from . models import *
from django.contrib import admin

class CustomRace(admin.ModelAdmin):
    list_display = ("title","start_date","end_date","category","race_manager")

admin.site.register(Category)
admin.site.register(Race,CustomRace)
from django.contrib import admin
from .models import Tag, Location, Activity, Report

for app in (Tag, Location, Activity, Report,):
    admin.site.register(app)

from django.contrib import admin
from .models import Tag, Activity, Report

for app in (Tag, Activity, Report,):
    admin.site.register(app)

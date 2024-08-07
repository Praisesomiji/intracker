from django.contrib import admin
from .models import Tag, Location, Activity, Report
from internship_tracker.admin import intern_ui

for model in (Tag, Location, Activity, Report,):
    admin.site.register(model)
    intern_ui.register(model)


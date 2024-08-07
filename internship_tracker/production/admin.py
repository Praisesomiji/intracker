from django.contrib import admin
from .models import Production, Feedback
from internship_tracker.admin import intern_ui

for model in (Production, Feedback,):
    admin.site.register(model)
    intern_ui.register(model)


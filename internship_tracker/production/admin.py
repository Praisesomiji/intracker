from django.contrib import admin
from .models import Production, Feedback

for app in (Production, Feedback,):
    admin.site.register(app)

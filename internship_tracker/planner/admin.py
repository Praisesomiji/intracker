from django.contrib import admin
from .models import Week, Unit, Instruction
from internship_tracker.admin import intern_ui

for model in (Week, Unit, Instruction,):
    admin.site.register(model)
    intern_ui.register(model)


from django.contrib import admin
from .models import Week, Unit, Instruction

for app in (Week, Unit, Instruction,):
    admin.site.register(app)

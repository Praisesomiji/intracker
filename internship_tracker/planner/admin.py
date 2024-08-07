from django.contrib import admin
from .models import Week, Unit, Instruction
from internship_tracker.admin import intern_ui

for model in (Week, Unit, Instruction,):
    admin.site.register(model)

class WeekAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class Instruction(admin.ModelAdmin):
    list_display = ('week', 

for ui in (
        {'model': Week, 'admin': WeekAdmin}, 
        {'model': Unit, 'admin': UnitAdmin,) 
        {'model': Instruction, 'admin': InstructionAdmin}
        ):
    intern_ui.register(ui['model'], ui['admin'])

from django.contrib import admin
from .models import Production, Feedback
from internship_tracker.admin import intern_ui

for app in (Production, Feedback,):
    admin.site.register(app)

class WeekAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

for ui in (
        {'model': Week, 'admin': WeekAdmin},
        {'model': Unit, 'admin': UnitAdmin,)
        {'model': Instruction, 'admin': InstructionAdmin}
        ):
    intern_ui.register(ui['model'], ui['admin'])

from django.contrib import admin
from .models import Workshop, Details

class DetailsInline(admin.TabularInline):
    model = Workshop.details.through
    extra = 1

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'about')
    inlines = [DetailsInline]

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'venue')


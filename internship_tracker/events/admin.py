from django.contrib import admin
from .models import Workshop, Details
from django.contrib.auth.models import User
from internship_tracker.admin import intern_ui

class DetailsInline(admin.TabularInline):
    model = Workshop.details.through
    extra = 1

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'related_details')
    search_fields = ('title', 'about')
    inlines = [DetailsInline]

    def related_details(self, obj):
        return ", ".join([f"{detail.date} {detail.time}" for detail in obj.details.all()])
    related_details.short_description = "Details"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(details__workshops__intern=request.user) | qs.filter(details__workshops__team__in=request.user.groups.all())

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'venue')
    search_fields = ('venue',)

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Details, DetailsAdmin)
intern_ui.register(Workshop, WorkshopAdmin)
intern_ui.register(Details, DetailsAdmin)


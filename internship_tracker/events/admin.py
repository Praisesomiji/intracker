from django.contrib import admin
from .models import Workshop, Detail
from internship_tracker.admin import intern_ui

class DetailInline(admin.TabularInline):
    model = Workshop.detail.through
    extra = 1

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'related_detail')
    search_fields = ('title', 'about')
    inlines = [DetailInline]

    def related_detail(self, obj):
        return ", ".join([f"{detail.date} {detail.time}" for detail in obj.detail.all()])
    related_detail.short_description = "Detail"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(detail__workshops__intern=request.user) | qs.filter(detail__workshops__team__in=request.user.groups.all())

class DetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'venue')
    search_fields = ('venue',)

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Detail, DetailAdmin)
intern_ui.register(Workshop, WorkshopAdmin)
intern_ui.register(Detail, DetailAdmin)


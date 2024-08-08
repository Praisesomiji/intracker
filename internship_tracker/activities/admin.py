from django.contrib import admin
from .models import Tag, Location, Activity, Report
from internship_tracker.admin import intern_ui
from production.models import Production

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('production', 'title', 'description', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(production__instruction__intern=request.user) | qs.filter(production__instruction__team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "production" and not request.user.is_superuser:
            kwargs["queryset"] = Production.objects.filter(instruction__intern=request.user) | Production.objects.filter(instruction__team__in=request.user.groups.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('activity', 'comment', 'type')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(activity__production__instruction__intern=request.user) | qs.filter(activity__production__instruction__team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "production" and not request.user.is_superuser:
            kwargs["queryset"] = Production.objects.filter(instruction__intern=request.user) | Production.objects.filter(instruction__team__in=request.user.groups.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


for site in (admin.site, intern_ui,):
    site.register(Activity, ActivityAdmin)
    site.register(Report, ReportAdmin)

for model in (Tag, Location,):
    admin.site.register(model)
    intern_ui.register(model)


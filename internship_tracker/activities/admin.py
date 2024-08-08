from django.contrib import admin
from .models import Tag, Location, Activity, Report
from internship_tracker.admin import intern_ui
from production.models import Production
from django.utils.html import format_html
from django.urls import reverse

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('production', 'title', 'description', 'location', 'reports')
    search_fields = ['title', 'description']

    def reports(self, obj):
        reports = obj.report_set.all()
        if reports.exists():
            links = [
                format_html(
                    '<a href="{}">{}</a>',
                    reverse("admin:activities_report_change", args=[report.pk], current_app=self.admin_site.name),
                    report.comment
                )
                for report in reports
            ]
            return format_html(", ".join(links))
        return "None"

    reports.short_description = "Reports"

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
    search_fields = ['type']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(activity__production__instruction__intern=request.user) | qs.filter(activity__production__instruction__team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "activity" and not request.user.is_superuser:
            kwargs["queryset"] = Activity.objects.filter(production__instruction__intern=request.user) | Activity.objects.filter(production__instruction__team__in=request.user.groups.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

for site in (admin.site, intern_ui,):
    site.register(Activity, ActivityAdmin)
    site.register(Report, ReportAdmin)

for model in (Tag, Location,):
    admin.site.register(model)
    intern_ui.register(model)


from django.contrib import admin
from .models import Production, Feedback
from internship_tracker.admin import intern_ui
from planner.models import Instruction
from django.utils.html import format_html
from django.urls import reverse

class ProductionAdmin(admin.ModelAdmin):
    list_display = ('instruction', 'description', 'deadline', 'submitted', 'feedbacks')

    def feedbacks(self, obj):
        feedbacks = obj.feedback_set.all()
        if feedbacks.exists():
            links = [
                format_html(
                    '<a href="{}">{}</a>',
                    reverse("admin:production_feedback_change", args=[feedback.pk], current_app=self.admin_site.name),
                    feedback.comment
                )
                for feedback in feedbacks
            ]
            return format_html(", ".join(links))
        return "None"

    feedbacks.short_description = "Feedbacks"

    def get_queryset(self, request):
        # Get the original queryset
        qs = super().get_queryset(request)
        # Superusers see everything
        if request.user.is_superuser:
            return qs
        # Interns see only productions where they are the insrtucted intern or part of the instructed team
        return qs.filter(instruction__intern=request.user) | qs.filter(instruction__team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # if the field is 'instruction', limit to instructions the logged in user is related to
        if db_field.name == "instruction" and not request.user.is_superuser:
            kwargs["queryset"] = Instruction.objects.filter(intern=request.user) | Instruction.objects.filter(team__in=request.user.groups.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('production', 'comment', 'swot')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(production__instruction__intern=request.user) | qs.filter(production__instruction__team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "production" and not request.user.is_superuser:
            kwargs["queryset"] = Production.objects.filter(instruction__intern=request.user) | Production.objects.filter(instruction__team__in=request.user.groups.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


for site in (admin.site, intern_ui,):
    site.register(Production, ProductionAdmin)
    site.register(Feedback, FeedbackAdmin)


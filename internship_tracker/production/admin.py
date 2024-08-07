from django.contrib import admin
from .models import Production, Feedback
from internship_tracker.admin import intern_ui

class ProductionAdmin(admin.ModelAdmin):
    list_display = ('instruction', 'description', 'deadline', 'submitted')

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

for site in (admin.site, intern_ui,):
    site.register(Production, ProductionAdmin)
    site.register(Feedback, FeedbackAdmin)


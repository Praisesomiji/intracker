from django.contrib import admin
from .models import Week, Unit, Instruction
from internship_tracker.admin import intern_ui
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Q

class WeekAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'instructions')
    search_fields = ['title']

    def instructions(self, obj):
        user = self.request.user  # Get the current user

        # Filter instructions based on the current user's permissions
        if user.is_superuser:
            instructions = obj.instruction_set.all()
        else:
            instructions = obj.instruction_set.filter(
                Q(intern=user) | Q(team__in=user.groups.all())
            ).distinct()

        if instructions.exists():
            links = [
                format_html(
                    '<a href="{}">{}</a>',
                    reverse("admin:planner_instruction_change", args=[instruction.pk], current_app=self.admin_site.name),
                    instruction.description
                )
                for instruction in instructions
            ]
            return format_html(", ".join(links))
        return "None"

    instructions.short_description = "Instructions"

    def get_queryset(self, request):
        """Override to make request available in instructions method."""
        self.request = request
        return super().get_queryset(request)


class InstructionAdmin(admin.ModelAdmin):
    list_display = ('week', 'product', 'intern', 'team', 'unit', 'description', 'productions')
    search_fields = ['description']

    def productions(self, obj):
        productions = obj.production_set.all()
        if productions.exists():
            links = [
                format_html(
                    '<a href="{}">{}</a>',
                    reverse("admin:production_production_change", args=[production.pk], current_app=self.admin_site.name),
                    production.description
                )
                for production in productions
            ]
            return format_html(", ".join(links))
        return "None"

    productions.short_description = "Productions"

    def get_queryset(self, request):
        # Get the original queryset
        qs = super().get_queryset(request)
        # Superusers see everything
        if request.user.is_superuser:
            return qs
        # Interns see only instructions where they are the intern or part of the team
        return qs.filter(intern=request.user) | qs.filter(team__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # If the field is 'intern', limit to the logged-in user (for interns)
        if db_field.name == "intern" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        # If the field is 'team', limit to groups the logged-in user is a member of
        if db_field.name == "team" and not request.user.is_superuser:
            kwargs["queryset"] = request.user.groups.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

for site in (admin.site, intern_ui,):
    site.register(Instruction, InstructionAdmin)
    site.register(Week, WeekAdmin)

admin.site.register(Unit)


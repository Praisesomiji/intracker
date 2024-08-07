from django.contrib import admin
from .models import Week, Unit, Instruction
from internship_tracker.admin import intern_ui
from django.contrib.auth.models import User, Group

class InstructionAdmin(admin.ModelAdmin):
    list_display = ('week', 'product', 'intern', 'team', 'unit', 'description')

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

for model in (Week, Unit,):
    admin.site.register(model)
    intern_ui.register(model)


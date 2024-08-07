from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

class CustomGroupAdmin(GroupAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

class InternAdminSite(AdminSite):
    site_header = ("Intern - Internship Tracker")
    site_title = ("Intern Site UI")
    index_title = ("Welcome to the Internship Tracker")

intern_ui = InternAdminSite(name='intern')
intern_ui.register(Group, CustomGroupAdmin)


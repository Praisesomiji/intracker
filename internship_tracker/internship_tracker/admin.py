# Import necessary modules
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin, GroupAdmin as DefaultGroupAdmin
from django.utils.translation import gettext_lazy as _

# Define a custom admin site for interns
class InternAdminSite(AdminSite):
    site_header = ("Internship Tracker")
    site_title = ("Intern Site UI")
    index_title = ("Welcome to the Internship Tracker")

# Create an instance of the custom admin site
intern_ui = InternAdminSite(name='intern')

# Define a custom UserAdmin class for the intern admin site
class UserAdmin(DefaultUserAdmin):
    # Define the fields to be displayed in the admin form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )

    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Define the fields that can be used to search for users
    search_fields = ('username', 'first_name', 'last_name', 'email')

    # Define the default ordering of the list view
    ordering = ('username',)

    # Override the get_queryset method to restrict interns to their own profile
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    # Override the get_readonly_fields method to make certain fields read-only for interns
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('username', 'password', 'is_active', 'is_staff', 'is_superuser', 'groups')
        return super().get_readonly_fields(request, obj)

# Register the custom UserAdmin class with the custom intern admin site
intern_ui.register(User, UserAdmin)

# Define a custom GroupAdmin class for the intern admin site
class GroupAdmin(DefaultGroupAdmin):
    # Override the get_form method to remove the permissions field for interns
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields.pop('permissions', None)
        return form

# Register the custom GroupAdmin class with the custom intern admin site
intern_ui.register(Group, GroupAdmin)


from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _

class InternAdminSite(AdminSite):
    site_header = _("Intern - Internship Tracker")
    site_title = _("Intern Site UI")
    index_title = _("Welcome to the Internship Tracker")

intern_ui = InternAdminSite(name='intern')


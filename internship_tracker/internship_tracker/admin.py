from django.contrib.admin import AdminSite

class InternAdminSite(AdminSite):
    site_header = ("Intern - Internship Tracker")
    site_title = ("Intern Site UI")
    index_title = ("Welcome to the Internship Tracker")

intern_ui = InternAdminSite(name='intern')


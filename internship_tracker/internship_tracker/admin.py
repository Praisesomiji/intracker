from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from planner.models import Week, Unit, Instruction
from production.models import Production, Feedback
from activities.model import Tag, Location, Activity, Report

class InternAdminSite(admin.AdminSite):
    site_header = _("Intern - Internship Tracker")
    site_title = _("Intern Site UI")
    index_title = _("Welcome to the Internship Tracker")

intern_ui = InternAdminSite(name='intern')


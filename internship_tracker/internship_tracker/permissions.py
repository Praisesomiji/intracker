from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from planner.models import Week, Instruction
from production.models import Production, Feedback
from activities.models import Activity, Report, Location

# Create or get the intern group
intern_group, created = Group.objects.get_or_create(name='All Interns Group')

# Get content types for the models
week_ct = ContentType.objects.get_for_model(Week)
instruction_ct = ContentType.objects.get_for_model(Instruction)
production_ct = ContentType.objects.get_for_model(Production)
feedback_ct = ContentType.objects.get_for_model(Feedback)
activity_ct = ContentType.objects.get_for_model(Activity)
report_ct = ContentType.objects.get_for_model(Report)

# Assign permissions to the intern group
permissions = [
    # Week permissions
    Permission.objects.get(codename='view_week', content_type=week_ct),
    # Instruction permissions
    Permission.objects.get(codename='view_instruction', content_type=instruction_ct),
    # Production permissions
    Permission.objects.get(codename='add_production', content_type=production_ct),
    Permission.objects.get(codename='view_production', content_type=production_ct),
    Permission.objects.get(codename='change_production', content_type=production_ct),
    Permission.objects.get(codename='delete_production', content_type=production_ct),
    # Feedback permissions
    Permission.objects.get(codename='add_feedback', content_type=feedback_ct),
    Permission.objects.get(codename='view_feedback', content_type=feedback_ct),
    Permission.objects.get(codename='change_feedback', content_type=feedback_ct),
    Permission.objects.get(codename='delete_feedback', content_type=feedback_ct),
    # Activity permissions
    Permission.objects.get(codename='add_activity', content_type=activity_ct),
    Permission.objects.get(codename='view_activity', content_type=activity_ct),
    Permission.objects.get(codename='change_activity', content_type=activity_ct),
    Permission.objects.get(codename='delete_activity', content_type=activity_ct),
    # Report permissions
    Permission.objects.get(codename='add_report', content_type=report_ct),
    Permission.objects.get(codename='view_report', content_type=report_ct),
    Permission.objects.get(codename='change_report', content_type=report_ct),
    Permission.objects.get(codename='delete_report', content_type=report_ct),
]

intern_group.permissions.set(permissions)

# Assign the intern group to a specific user
user = User.objects.get(username='intern-PHIL')  # replace with the intern's username
user.groups.add(intern_group)


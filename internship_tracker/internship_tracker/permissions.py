from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from planner.models import Week, Instruction
from production.models import Production, Feedback
from activities.models import Activity, Report

def assign_permissions():
    # Create or get the intern group
    intern_group, created = Group.objects.get_or_create(name='Interns')

    # Get content types for the models
    models = [Week, Instruction, Production, Feedback, Activity, Report, Group, User]
    content_types = {model.__name__.lower(): ContentType.objects.get_for_model(model) for model in models}

    # Define required permissions
    permissions = [
        ('view_week', 'week'),
        ('view_instruction', 'instruction'),
        ('add_production', 'production'),
        ('view_production', 'production'),
        ('change_production', 'production'),
        ('delete_production', 'production'),
        ('add_feedback', 'feedback'),
        ('view_feedback', 'feedback'),
        ('change_feedback', 'feedback'),
        ('delete_feedback', 'feedback'),
        ('add_activity', 'activity'),
        ('view_activity', 'activity'),
        ('change_activity', 'activity'),
        ('delete_activity', 'activity'),
        ('add_report', 'report'),
        ('view_report', 'report'),
        ('change_report', 'report'),
        ('delete_report', 'report'),
        ('view_group', 'group'),
        ('view_user', 'user'),
    ]

    # Assign permissions to the intern group
    for codename, model in permissions:
        permission = Permission.objects.filter(codename=codename, content_type=content_types[model])
        if permission.exists():
            intern_group.permissions.add(permission.first())

    # Assign the intern group to a specific user
    user = User.objects.get(username='intern-PHIL') 
    user.groups.add(intern_group)


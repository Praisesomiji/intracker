from django.apps import AppConfig

class PlannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'planner'

    def ready(self):
        from internship_tracker.permissions import assign_permissions
        assign_permissions()

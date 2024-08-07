from django.shortcuts import redirect
from django.urls import reverse

# Access control for admin sites
class RoleBasedAccessMiddleware:
    """
    Prevent non-superusers from interacting with the admin site;
    Redirect superusers to the admin site
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return redirect(reverse('intern:login'))
        if request.path.startswith('/intern/') and request.user.is_superuser:
            return redirect(reverse('admin:login'))
        return self.get_response(request)



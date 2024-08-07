"""
URL configuration for internship_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from internship_tracker.admin import intern_ui

def redirect_to_proper_admin(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.groups.filter(name='interns').exists():
        return redirect('/intern/')
    return redirect('/intern/login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intern/', intern_ui.urls),
    path('', redirect_to_proper_admin),
]


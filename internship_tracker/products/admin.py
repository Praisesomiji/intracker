from django.contrib import admin
from .models import Product
from internship_tracker.admin import intern_ui

admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'class_type')

intern_ui.register(Product, ProductionAdmin)

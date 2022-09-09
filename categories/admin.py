from django.contrib import admin

from categories.models import Category


@admin.register(Category)
class BillingDataAdmin(admin.ModelAdmin):
    """Configure BillingData in Admin interface: export list, search and filter operations"""

    list_display = ('category_name',)


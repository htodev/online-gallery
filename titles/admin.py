from django.contrib import admin

from titles.models import Title


# admin.site.register(Category)

@admin.register(Title)
class BillingDataAdmin(admin.ModelAdmin):

    list_display = ('title_name',)

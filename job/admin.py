from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company_name",
        "employment_type",
    )
    search_fields = (
        "title",
        "company_name",
    )


admin.site.register(Job, JobAdmin)

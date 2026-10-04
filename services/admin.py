from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'name_marathi',
        'category',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'category',
    )

    search_fields = (
        'name',
        'name_marathi',
        'description',
    )

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'name_marathi',
                'description',
            )
        }),
        ('Service Details', {
            'fields': (
                'documents_required',
                'category',
            )
        }),
        ('Status', {
            'fields': (
                'is_active',
            )
        }),
    )
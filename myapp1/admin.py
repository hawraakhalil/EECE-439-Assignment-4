from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "tel_number", "profession", "address")
    search_fields = ("id", "name", "email", "profession", "address")
    list_filter = ("profession",)
    ordering = ("name",)
    readonly_fields = ("id",)
    fields = ("id", "name", "address", "profession", "tel_number", "email")
    list_display_links = ("id", "name")

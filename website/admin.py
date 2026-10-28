from django.contrib import admin
from .models import ProfilOrganisasi


@admin.register(ProfilOrganisasi)
class ProfilOrganisasiAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_singkat", "email")
    search_fields = ("nama", "nama_singkat", "email")


from django.contrib import admin
from .models import ProfilOrganisasi, Pimpinan
from .models import ProfilOrganisasi, Pimpinan, PimpinanRanting

@admin.register(ProfilOrganisasi)
class ProfilOrganisasiAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_singkat", "email")
    search_fields = ("nama", "nama_singkat", "email")


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "periode", "urutan")
    list_filter = ("periode", "jabatan")
    search_fields = ("nama", "jabatan")
    ordering = ("urutan", "nama")

@admin.register(PimpinanRanting)
class PimpinanRantingAdmin(admin.ModelAdmin):
    list_display = ("nama", "ketua", "alamat", "telepon")
    search_fields = ("nama", "ketua")
    ordering = ("urutan", "nama")
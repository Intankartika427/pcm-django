from django.contrib import admin

from .models import (
    ProfilOrganisasi,
    Pimpinan,
    PimpinanRanting,
    AmalUsaha,
    Berita,
    Agenda,
)


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


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ("nama", "bidang", "alamat")
    list_filter = ("bidang",)
    search_fields = ("nama", "alamat")


@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = (
        "judul",
        "penulis",
        "tanggal_publikasi",
        "dipublikasikan",
    )
    list_filter = ("dipublikasikan", "tanggal_publikasi")
    search_fields = ("judul", "ringkasan", "isi", "penulis")
    prepopulated_fields = {"slug": ("judul",)}


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("nama_kegiatan", "waktu_mulai", "tempat")
    list_filter = ("waktu_mulai",)
    search_fields = ("nama_kegiatan", "tempat", "keterangan")
    ordering = ("-waktu_mulai",)
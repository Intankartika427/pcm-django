from django.contrib import admin

from .models import (
    ProfilOrganisasi,
    Pimpinan,
    PimpinanRanting,
    AmalUsaha,
    Berita,
    Agenda,
    Dokumen,
    TautanTerkait,
    PesanMasuk,
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


@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = (
        "judul",
        "tanggal_upload",
        "dipublikasikan",
    )
    list_filter = ("dipublikasikan", "tanggal_upload")
    search_fields = ("judul", "deskripsi")
    ordering = ("-tanggal_upload",)

@admin.register(TautanTerkait)
class TautanTerkaitAdmin(admin.ModelAdmin):
    list_display = (
        "nama",
        "url",
        "urutan",
        "aktif",
    )
    list_filter = ("aktif",)
    search_fields = ("nama", "deskripsi")
    ordering = ("urutan", "nama")


@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = (
        "nama",
        "email",
        "subjek",
        "waktu_kirim",
        "sudah_dibaca",
    )

    list_filter = ("sudah_dibaca", "waktu_kirim")
    search_fields = ("nama", "email", "subjek", "pesan")
    readonly_fields = (
        "nama",
        "email",
        "subjek",
        "pesan",
        "waktu_kirim",
    )
    ordering = ("-waktu_kirim",)


from django.shortcuts import render, get_object_or_404

from .models import (
    ProfilOrganisasi,
    Pimpinan,
    PimpinanRanting,
    AmalUsaha,
    Berita,
)


def home(request):
    profil = ProfilOrganisasi.objects.first()
    daftar_pimpinan = Pimpinan.objects.all()
    daftar_ranting = PimpinanRanting.objects.all()
    daftar_amal_usaha = AmalUsaha.objects.all()

    berita_terbaru = Berita.objects.filter(
        dipublikasikan=True
    ).order_by("-tanggal_publikasi")[:3]

    context = {
        "profil": profil,
        "daftar_pimpinan": daftar_pimpinan,
        "daftar_ranting": daftar_ranting,
        "daftar_amal_usaha": daftar_amal_usaha,
        "berita_terbaru": berita_terbaru,
    }

    return render(request, "website/home.html", context)


def daftar_berita(request):
    berita = Berita.objects.filter(
        dipublikasikan=True
    ).order_by("-tanggal_publikasi")

    context = {
        "daftar_berita": berita,
    }

    return render(request, "website/berita_list.html", context)


def detail_berita(request, slug):
    berita = get_object_or_404(
        Berita,
        slug=slug,
        dipublikasikan=True,
    )

    context = {
        "berita": berita,
    }

    return render(request, "website/berita_detail.html", context)

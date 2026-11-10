from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PesanMasukForm

from .models import (
    ProfilOrganisasi,
    Pimpinan,
    PimpinanRanting,
    AmalUsaha,
    Berita,
    Agenda,
    Dokumen,
    TautanTerkait,
)

def profil(request):
    data_profil = ProfilOrganisasi.objects.first()

    context = {
        "profil": data_profil,
    }

    return render(request, "website/profil.html", context)

def daftar_pimpinan(request):
    daftar_pimpinan = Pimpinan.objects.all()
    context = {
        "daftar_pimpinan": daftar_pimpinan,
    }
    return render(request, "website/pimpinan.html", context)

def daftar_ranting(request):
    daftar_ranting = PimpinanRanting.objects.all()

    context = {
        "daftar_ranting": daftar_ranting,
    }

    return render(request, "website/ranting.html", context)

def home(request):
    profil = ProfilOrganisasi.objects.first()
    daftar_pimpinan = Pimpinan.objects.all()
    daftar_ranting = PimpinanRanting.objects.all()
    daftar_amal_usaha = AmalUsaha.objects.all()

    daftar_agenda = Agenda.objects.all().order_by("-waktu_mulai")

    berita_terbaru = Berita.objects.filter(
        dipublikasikan=True
    ).order_by("-tanggal_publikasi")[:3]

    context = {
        "profil": profil,
        "daftar_pimpinan": daftar_pimpinan,
        "daftar_ranting": daftar_ranting,
        "daftar_amal_usaha": daftar_amal_usaha,
        "berita_terbaru": berita_terbaru,
        "daftar_agenda": daftar_agenda,
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

def daftar_agenda(request):
    agenda = Agenda.objects.all().order_by("-waktu_mulai")

    context = {
        "daftar_agenda": agenda,
        "now": timezone.now(),
    }

    return render(request, "website/agenda_list.html", context)


def daftar_dokumen(request):
    dokumen = Dokumen.objects.filter(
        dipublikasikan=True
    ).order_by("-tanggal_upload")

    context = {
        "daftar_dokumen": dokumen,
    }

    return render(request, "website/unduhan.html", context)

def daftar_tautan(request):
    tautan = TautanTerkait.objects.filter(
        aktif=True
    ).order_by("urutan")

    context = {
        "daftar_tautan": tautan,
    }

    return render(
        request,
        "website/tautan.html",
        context,
    )


def kirim_pesan(request):
    if request.method == "POST":
        form = PesanMasukForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Pesan Anda berhasil dikirim. Terima kasih!"
            )
            return redirect("website:kirim_pesan")
    else:
        form = PesanMasukForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "website/kirim_pesan.html",
        context,
    )


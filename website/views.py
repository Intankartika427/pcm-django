
from django.shortcuts import render
from .models import ProfilOrganisasi, Pimpinan, PimpinanRanting, AmalUsaha


def home(request):
    profil = ProfilOrganisasi.objects.first()
    daftar_pimpinan = Pimpinan.objects.all()
    daftar_ranting = PimpinanRanting.objects.all()
    daftar_amal_usaha = AmalUsaha.objects.all()

    context = {
        "profil": profil,
        "daftar_pimpinan": daftar_pimpinan,
        "daftar_ranting": daftar_ranting,
        "daftar_amal_usaha": daftar_amal_usaha,
    }

    return render(request, "website/home.html", context)
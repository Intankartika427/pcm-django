
from django.shortcuts import render
from .models import ProfilOrganisasi, Pimpinan, PimpinanRanting


def home(request):
    profil = ProfilOrganisasi.objects.first()
    daftar_pimpinan = Pimpinan.objects.all()
    daftar_ranting = PimpinanRanting.objects.all()

    context = {
        "profil": profil,
        "daftar_pimpinan": daftar_pimpinan,
        "daftar_ranting": daftar_ranting,
    }

    return render(request, "website/home.html", context)


from django.shortcuts import render
from .models import ProfilOrganisasi, Pimpinan


def home(request):
    profil = ProfilOrganisasi.objects.first()
    daftar_pimpinan = Pimpinan.objects.all()

    context = {
        "profil": profil,
        "daftar_pimpinan": daftar_pimpinan,
    }

    return render(request, "website/home.html", context)

from django.shortcuts import render
from .models import ProfilOrganisasi


def home(request):
    profil = ProfilOrganisasi.objects.first()

    context = {
        "profil": profil,
    }

    return render(request, "website/home.html", context)

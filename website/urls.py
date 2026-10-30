
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
     path("profil/", views.profil, name="profil"),
     path("pimpinan/", views.daftar_pimpinan, name="pimpinan"),
     path("ranting/", views.daftar_ranting, name="ranting"),
    path("berita/", views.daftar_berita, name="daftar_berita"),
    path(
        "berita/<slug:slug>/",
        views.detail_berita,
        name="detail_berita",
    ),
    path("agenda/", views.daftar_agenda, name="daftar_agenda"),
    
]

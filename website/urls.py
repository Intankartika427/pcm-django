
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("berita/", views.daftar_berita, name="daftar_berita"),
    path(
        "berita/<slug:slug>/",
        views.detail_berita,
        name="detail_berita",
    ),
]

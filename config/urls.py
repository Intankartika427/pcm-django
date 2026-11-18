from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]

# Layani /media/ dari disk hanya jika media TIDAK disimpan di Supabase Storage.
# Di produksi (USE_SUPABASE_STORAGE=True) URL gambar langsung mengarah ke storage,
# jadi route ini tidak dipakai.
if not settings.USE_SUPABASE_STORAGE:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]
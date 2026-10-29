from django.db import models


class ProfilOrganisasi(models.Model):
    nama = models.CharField(max_length=200)
    nama_singkat = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255, blank=True)
    deskripsi = models.TextField(blank=True)
    sejarah = models.TextField(blank=True)
    visi = models.TextField(blank=True)
    misi = models.TextField(blank=True)
    alamat = models.TextField(blank=True)
    telepon = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    gambar = models.ImageField(
        upload_to="profil/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Profil Organisasi"
        verbose_name_plural = "Profil Organisasi"

    def __str__(self):
        return self.nama


class Pimpinan(models.Model):
    nama = models.CharField(max_length=200)
    jabatan = models.CharField(max_length=100)
    periode = models.CharField(max_length=20, default="2022–2027")
    foto = models.ImageField(
        upload_to="pimpinan/",
        blank=True,
        null=True,
    )
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Pimpinan"
        verbose_name_plural = "Data Pimpinan"
        ordering = ["urutan", "nama"]

    def __str__(self):
        return f"{self.nama} - {self.jabatan}"

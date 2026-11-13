
from datetime import datetime
from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import (
    ProfilOrganisasi,
    Pimpinan,
    PimpinanRanting,
    AmalUsaha,
    Berita,
    Agenda,
    TautanTerkait,
)


class Command(BaseCommand):
    help = "Memasukkan data awal PCM Solo Utara"

    def handle(self, *args, **options):
        self.stdout.write("Memulai pengisian data PCM Solo Utara...")

        # 1. PROFIL ORGANISASI
        profil, created = ProfilOrganisasi.objects.update_or_create(
            nama_singkat="PCM Solo Utara",
            defaults={
                "nama": "Pimpinan Cabang Muhammadiyah Solo Utara",
                "tagline": "Bergerak Mencerahkan, Berkhidmat Untuk Umat",
                "deskripsi": (
                    "PCM Solo Utara adalah salah satu cabang organisasi "
                    "Muhammadiyah di Kota Surakarta, Jawa Tengah."
                ),
                "sejarah": (
                    "PCM Solo Utara merupakan bagian dari perkembangan "
                    "Muhammadiyah di Kota Surakarta. Organisasi ini "
                    "mengayomi delapan Pimpinan Ranting Muhammadiyah "
                    "di wilayah Solo Utara."
                ),
                "visi": "",
                "misi": "",
                "alamat": "Jl. Singosari Utara I No. 13, Nusukan, Surakarta",
                "telepon": "0857-0245-1925 / 0877-3460-5640",
                "email": "pcmsoloutara@gmail.com",
            },
        )

        if not profil.gambar:
            profil.gambar = "profil/Logo_PCM_Solo_Utara.jpg"
            profil.save()

        # 2. DATA PIMPINAN
        pimpinan_data = [
            ("Abdul Mutolib, S.Ag, M.Ag", "Ketua"),
            ("Ir. H. Suhendro Trinugroho, M.T.", "Wakil Ketua"),
            ("Puryadi", "Sekretaris"),
            ("Sogi Agung Sanoto, S.Pd", "Wakil Sekretaris"),
            ("Sumarman, S.Ag, M.Ag", "Bendahara"),
            ("H. Ahmad Sukidi, S.Ag, M.Pd", "Wakil Bendahara"),
            ("dr. Bambang Sutanto, SpAn, -KIC", "Anggota"),
            ("Drs. H. Ridwan Sukimin", "Anggota"),
            ("H. M. Saidi B.A.", "Anggota"),
            ("Muhammad Nashir, S.Ag.", "Anggota"),
            ("H. Alqaf Hudaya, S.H.", "Anggota"),
            ("Agus Sutejo, S.Sn.", "Anggota"),
            ("Drs. H. Yatimun", "Anggota"),
        ]

        for nomor, (nama, jabatan) in enumerate(pimpinan_data, start=1):
            pimpinan, _ = Pimpinan.objects.update_or_create(
                nama=nama,
                defaults={
                    "jabatan": jabatan,
                    "periode": "2022-2027",
                    "urutan": nomor,
                },
            )

            if nama == "Abdul Mutolib, S.Ag, M.Ag" and not pimpinan.foto:
                pimpinan.foto = "pimpinan/Foto_KetuaPCM.jpeg"
                pimpinan.save()

        # 3. DATA PIMPINAN RANTING
        ranting_data = [
            (
                "PRM Kota Pasir",
                "Masjid Subulus Salam, Komplang RT 03/RW 26, Kadipiro, Surakarta",
            ),
            (
                "PRM Sruni",
                "SD Muhammadiyah 22, Jl. Samudra Pasai II, Sruni, Kadipiro, Banjarsari, Surakarta",
            ),
            (
                "PRM Sekip",
                "Masjid Al Fatah, Jl. Kolonel Sugiyono, Sekip, Kadipiro, Surakarta",
            ),
            (
                "PRM Sumber Nayu",
                "Kompleks Masjid Riyadhoh Iman, Jl. Kolonel Sugiyono No. 53, Kadipiro, Surakarta",
            ),
            (
                "PRM Nusukan Timur",
                "Masjid Al Amin, Bubisluhur, Surakarta",
            ),
            (
                "PRM Nusukan",
                "Masjid Al Muttaqien, Jl. Jenggolo IV, RT 03/RW 26, Praon, Nusukan, Surakarta",
            ),
            (
                "PRM Banyuanyar",
                "Jl. Adisumarmo No. 182, Banyuanyar, Surakarta",
            ),
            (
                "PRM Kadipiro",
                "Masjid Baitul Ghufron, Jl. Tulang Bawang Tengah, Tegalsari, Surakarta",
            ),
        ]

        for nomor, (nama, alamat) in enumerate(ranting_data, start=1):
            PimpinanRanting.objects.update_or_create(
                nama=nama,
                defaults={
                    "alamat": alamat,
                    "ketua": "",
                    "telepon": "",
                    "urutan": nomor,
                },
            )

        # 4. AMAL USAHA
        amal_usaha_data = [
            {
                "nama": "SD Muhammadiyah 3 Surakarta",
                "bidang": "pendidikan",
                "alamat": "Jl. Singosari Utara I No. 13, Nusukan, Surakarta",
                "deskripsi": (
                    "Sekolah dasar Islam yang mengembangkan pendidikan "
                    "berlandaskan IMTAQ dan IPTEK, dengan pembiasaan "
                    "murotal, tahfidz Al-Qur'an, salat berjamaah, "
                    "dan kegiatan keagamaan."
                ),
            },
            {
                "nama": "SMP Muhammadiyah 2 Surakarta",
                "bidang": "pendidikan",
                "alamat": "Jl. Kerinci No. 15, Banjarsari, Surakarta",
                "deskripsi": (
                    "Sekolah menengah pertama swasta Islam yang "
                    "mengintegrasikan pendidikan modern dengan "
                    "nilai-nilai Islami dan Program Adiwiyata."
                ),
            },
            {
                "nama": "SMK Muhammadiyah 5 Surakarta",
                "bidang": "pendidikan",
                "alamat": "Jl. Kerinci, Banjarsari, Surakarta",
                "deskripsi": (
                    "Sekolah menengah kejuruan swasta yang dikenal "
                    "dengan julukan Mulia of Art | Fashion Design School."
                ),
            },
            {
                "nama": "Universitas Muhammadiyah PKU Surakarta",
                "bidang": "pendidikan",
                "alamat": "Jl. Tulang Bawang Selatan No. 26, Kadipiro, Surakarta",
                "deskripsi": (
                    "Perguruan tinggi swasta di Kota Surakarta yang "
                    "dikelola oleh Persyarikatan Muhammadiyah."
                ),
            },
            {
                "nama": "Toko Amaliyah Q-ta",
                "bidang": "ekonomi",
                "alamat": "Jl. Samudra Pasai, Komplang, Kadipiro, Surakarta",
                "deskripsi": (
                    "Toko ritel kebutuhan masyarakat yang berada "
                    "di lingkungan PCM Solo Utara."
                ),
            },
            {
                "nama": "Lazismu",
                "bidang": "sosial",
                "alamat": "Jl. Popda, Nusukan, Banjarsari, Surakarta",
                "deskripsi": (
                    "Lembaga yang menjalankan kegiatan pemberdayaan "
                    "ekonomi, pendidikan, sosial kemanusiaan, dan dakwah."
                ),
            },
        ]

        for data in amal_usaha_data:
            AmalUsaha.objects.update_or_create(
                nama=data["nama"],
                defaults=data,
            )

        # 5. BERITA
        Berita.objects.update_or_create(
            slug="pcm-solo-utara-gelar-hari-bermuhammadiyah-hadirkan-wayang-golek-pitutur-17363",
            defaults={
                "judul": (
                    "PCM Solo Utara Gelar Hari BerMuhammadiyah, "
                    "Hadirkan Wayang Golek Pitutur"
                ),
                "ringkasan": (
                    "PCM Solo Utara menggelar Hari BerMuhammadiyah "
                    "dengan pengajian Meneladan Nabi, Mencerahkan "
                    "Negeri dan dakwah melalui Wayang Golek Pitutur."
                ),
                "isi": (
                    "Pimpinan Cabang Muhammadiyah Solo Utara, Kota Solo, "
                    "menggelar Hari BerMuhammadiyah pada Ahad, "
                    "6 September 2026. Kegiatan menghadirkan pengajian "
                    "Meneladan Nabi, Mencerahkan Negeri bersama "
                    "Ust. Pujiono, dai Wayang Golek Pitutur dari "
                    "Majelis Tabligh PWM. Kegiatan juga dilengkapi "
                    "layanan kesehatan dan bazar murah."
                ),
                "penulis": "",
                "dipublikasikan": True,
            },
        )

        berita = Berita.objects.get(
            slug="pcm-solo-utara-gelar-hari-bermuhammadiyah-hadirkan-wayang-golek-pitutur-17363"
        )
        if not berita.gambar:
            berita.gambar = "berita/Picture10.png"
            berita.save()

        # 6. AGENDA
        zona = ZoneInfo("Asia/Jakarta")

        agenda_data = [
            {
                "nama_kegiatan": (
                    "Pengajian SENIN MALAM PCM Solo Utara "
                    "#Pekan ke-2 Oktober 2026"
                ),
                "waktu_mulai": datetime(2026, 10, 12, 20, 0, tzinfo=zona),
                "tempat": (
                    "Masjid At Taqwa, Jl. Tarumanegara II No. 29, "
                    "Banyuanyar, Banjarsari, Surakarta"
                ),
                "keterangan": (
                    "Tema KEMUHAMMADIYAHAN bersama "
                    "K.H. Ali Muhson, M.Ag., M.M."
                ),
            },
            {
                "nama_kegiatan": (
                    "Pengajian Senin Malam PCM Solo Utara: "
                    "Adab Seorang Muslim"
                ),
                "waktu_mulai": datetime(2026, 9, 28, 20, 0, tzinfo=zona),
                "tempat": (
                    "Masjid Al Fitroh, Jl. Popda, Nusukan, "
                    "Banjarsari, Surakarta"
                ),
                "keterangan": (
                    "Bersama Al-Ust. Wahyudi Umar A. al-Hafidz, M.Pd. "
                    "Acara terbuka untuk umum."
                ),
            },
            {
                "nama_kegiatan": (
                    "Pengajian Akbar Hari BerMuhammadiyah: "
                    "Meneladani Nabi, Mencerahkan Negeri"
                ),
                "waktu_mulai": datetime(2026, 9, 6, 6, 0, tzinfo=zona),
                "tempat": (
                    "Masjid Al Amin Bibis Luhur, PRM Nusukan Timur, "
                    "Surakarta"
                ),
                "keterangan": (
                    "Bersama Ust. Pujiono. Dimeriahkan cek kesehatan "
                    "gratis, stan pendidikan dan bazar sembako murah."
                ),
            },
        ]

        for data in agenda_data:
            Agenda.objects.update_or_create(
                nama_kegiatan=data["nama_kegiatan"],
                defaults=data,
            )

        # 7. TAUTAN TERKAIT
        tautan_data = [
            {
                "nama": "LPCR PM PDM Surakarta",
                "url": "https://lpcrpmpdmsurakarta.or.id/",
                "deskripsi": "LPCRPM PDM Surakarta",
                "urutan": 1,
                "aktif": True,
            },
            {
                "nama": "Pimpinan Daerah Muhammadiyah Kota Surakarta",
                "url": (
                    "https://muhammadiyahjateng.or.id/"
                    "pimpinan-daerah-muhammadiyah-kota-surakarta/"
                ),
                "deskripsi": "Informasi PDM Kota Surakarta",
                "urutan": 2,
                "aktif": True,
            },
        ]

        for data in tautan_data:
            TautanTerkait.objects.update_or_create(
                nama=data["nama"],
                defaults=data,
            )

        # RINGKASAN
        self.stdout.write(self.style.SUCCESS(
            "Seed PCM Solo Utara berhasil dijalankan!"
        ))

        self.stdout.write(
            f"Profil Organisasi : {ProfilOrganisasi.objects.count()}"
        )
        self.stdout.write(
            f"Pimpinan          : {Pimpinan.objects.count()}"
        )
        self.stdout.write(
            f"Pimpinan Ranting  : {PimpinanRanting.objects.count()}"
        )
        self.stdout.write(
            f"Amal Usaha        : {AmalUsaha.objects.count()}"
        )
        self.stdout.write(
            f"Berita            : {Berita.objects.count()}"
        )
        self.stdout.write(
            f"Agenda            : {Agenda.objects.count()}"
        )
        self.stdout.write(
            f"Tautan Terkait    : {TautanTerkait.objects.count()}"
        )

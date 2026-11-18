# Website Pimpinan Cabang Muhammadiyah Solo Utara
Tugas kelompok mata kuliah **Pemrograman Web berbasis Framework (TIF1336)**.
> **Catatan:**  Website ini merupakan proyek pengembangan website profil Pimpinan Cabang Muhammadiyah (PCM) Solo Utara, Surakarta, sebagai bagian dari tugas akademik. Website bertujuan menyajikan informasi organisasi, pimpinan, ranting, amal usaha, berita, dan agenda kegiatan PCM Solo Utara, **bukan website resmi** Pimpinan Cabang Muhammadiyah (PCM) SOLO UTARA

---

Oleh : Kelompok K Pemrograman WEB Berbasis Framework
| No. | Nama Anggota | NIM |
| --- | --- | --- |
| 1 | M. Hafiz Azahari Y | L200210234 |
| 2 | Raihan Daffa A.S | L200230278 |
| 3 | Muhammad Fadhlan | L200230285 |
| 4 | Intan Kartika Sari | L200240006 |
| 5 | Zola Icha Shafira | L200240032 |

## 1. PCM yang Dipilih
- **Nama:** PCM Solo Utara
- **Wilayah:** Banjarsari, Surakarta, Jawa Tengah
### Tabel Sumber Data
| No. | Data | Sumber | Tanggal Pengambilan |
| --- | --- | --- | --- |
| 1 | Profil PCM Solo Utara | Wawancara/konfirmasi pengurus PCM Solo Utara | 24 Oktober 2026 |
| 2 | Sejarah PCM Solo Utara | Instagram PCM Solo Utara | 21 Oktober 2026 |
| 3 | Susunan pimpinan | Wawancara/konfirmasi pengurus PCM Solo Utara | 24 Oktober 2026 |
| 4 | Informasi ranting | Wawancara/konfirmasi pengurus PCM Solo Utara | 24 Oktober 2026 |
| 5 | Amal usaha Muhammadiyah | Wawancara/konfirmasi pengurus dan sumber daring | 24 Oktober 2026 |
| 6 | Berita Hari BerMuhammadiyah | Website Muhammadiyah Solo | 27 Oktober 2026 |
| 7 | Agenda kegiatan | Instagram PCM Solo Utara | 27 Oktober 2026 |
| 8 | Foto pengurus, kegiatan, dan bangunan | Dokumentasi PCM Solo Utara | 27 Oktober 2026 |

### Perizinan Penggunaan Data dan Dokumentasi
Penggunaan foto pengurus, kegiatan, dan bangunan PCM Solo Utara pada proyek ini telah memperoleh izin dari:
- **Nama:** Bapak Abdul Mutolib
- **Jabatan:** Ketua Pimpinan Cabang Muhammadiyah Solo Utara
- **Tanggal konfirmasi:** 22 Oktober 2026
## 2. Tabel Kontribusi
| No. | Nama | NIM | Tanggung Jawab |
| --- | --- | --- | --- |
| 1 | Intan Kartika Sari | L200240006 | 1. Pengumpulan dan pencarian data informasi PCM<br>2. Inisialisasi proyek Django dan pengembangan fondasi website<br>3. Pembuatan template dan CSS<br>4. Pengembangan halaman utama<br>5. Pembuatan fitur profil organisasi<br>6. Pembuatan fitur Pimpinan<br>7. Pembuatan fitur Ranting<br>8. Docker dan PostgreSQL<br>9. Penulisan data Readme<br>10. Pembuatan Video |
| 2 | Zola Icha Shafira | L200240032 | 1. Pengumpulan dan pencarian data informasi PCM<br>2. Pembuatan fitur Amal Usaha<br>3. Pembuatan fitur Berita<br>4. Pembuatan fitur Agenda Kegiatan<br>5. Docker<br>6. Pembuatan PPT<br>7. Pembuatan Video |
| 3 | Muhammad Fadhlan | L200230285 | 1. Pembuatan fitur Dokumen<br>2. Pembuatan fitur Pesan Masuk<br>3. Docker dan PostgreSQL<br>4. Deployment<br>5. Pembuatan Video |
| 4 | Raihan Daffa A.S | L200230278 | 1. Pembuatan fitur Tautan Terkait<br>2. Docker dan PostgreSQL<br>3. Deployment<br>4. Pembuatan Video |
| 5 | M. Hafiz Azhari Y | L200210234 | 1. Docker<br>2. Pembuatan Video |

## 3. Cara Menjalankan Proyek
### Langkah Instalasi (Dengan `uv`)
1. Clone repository:
```bash
git clone https://github.com/Intankartika427/pcm-django.git
```
2. Masuk ke folder proyek:
```bash
cd pcm-django
```
3. Instal dependensi:
```bash
uv sync
```
4. Jalankan migrasi database:
```bash
uv run python manage.py migrate
```
5. Jalankan server pengembangan:
```bash
uv run python manage.py runserver
```
6. Buka alamat berikut pada browser: `http://127.0.0.1:8000/`

### Dengan Docker
- **Persiapan:** Clone repository.
- **Menjalankan aplikasi:**
```bash
docker compose up --build
```
- **Membuka terminal baru**
- **Mengisi data awal:**
```bash
docker compose exec web uv run python manage.py seed_pcm
```
- **Membuka localhost:8000 di browser**
- **Membuat akun admin:**
```bash
docker compose exec web uv run python manage.py createsuperuser
```
- **Menghentikan container:**
```bash
docker compose down
```
- **Menghapus container dan seluruh volume:**
```bash
docker compose down -v
```
- Perintah `docker compose down` mempertahankan named volume sehingga database dan media tetap tersedia ketika container dijalankan kembali.
- Perintah `docker compose down -v` menghapus named volume, termasuk database dan media yang tersimpan di dalamnya.
- Perintah `docker compose down -v` dapat menghapus semua data karena opsi -v memerintahkan Docker untuk menghapus volume yang digunakan oleh container dalam konfigurasi Docker Compose tersebut, termasuk volume database PostgreSQL.
## 4. URL Produksi, Platform, dan Database yang Dipilih
- **URL Produksi:** https://pcm-django-production.up.railway.app/
- **Platform:** Railway, alasannya yaitu karena platform ini menyediakan pengalaman pengembangan yang lebih sederhana dan cepat. Dengan Railway, pengembang dapat dengan mudah menghubungkan GitHub repository mereka dan memulai deploy aplikasi tanpa harus mengelola server secara manual. Railway juga menawarkan manajemen database yang otomatis dan pengaturan variabel pengembangan yang aman, sehingga memudahkan pengelolaan keamanan dan konsistensi. Selain itu, Railway mendukung deploy aplikasi dari Docker dan menawarkan template yang memudahkan pengembang untuk memulai dengan aplikasi yang telah dipersiapkan.
- **Database:** Supabase, alasannya yaitu Supabase memungkinkan pengembang untuk membangun aplikasi dengan cepat dan efisien.
## 5. Daftar Environment Variable yang Dibutuhkan
| Variable | Keterangan |
| --- | --- |
| `SECRET_KEY` | Wajib di produksi; jangan pernah di-commit |
| `DEBUG` | `True` di laptop, `False` di produksi |
| `ALLOWED_HOSTS` | Daftar domain, dipisah koma |
| `CSRF_TRUSTED_ORIGINS` | Domain produksi lengkap dengan `https://` |
| `DATABASE_URL` | Kosong → SQLite; berisi URL PostgreSQL → database cloud (pakai `dj-database-url`) |

## 6. Teknologi yang Digunakan
| Komponen | Teknologi |
| --- | --- |
| Bahasa pemrograman | Python 3.14 |
| Framework | Django 6.x |
| Frontend | Django Template, CSS |
| Database lokal | SQLite |
| Database Docker | PostgreSQL 17 |
| Container | Docker Compose |
| Deployment | Railway |
| Database produksi | Supabase |
| Web server | Gunicorn |
| Static files | WhiteNoise |
| Media storage | Supabase Storage (S3) |

## 7. Fitur Website
- Beranda
- Profil organisasi
- Data pimpinan
- Data ranting
- Amal usaha
- Berita dan detail berita
- Agenda kegiatan
- Unduhan dokumen
- Formulir kontak
- Panel admin Django
## 8. Penutup
Proyek ini dikembangkan untuk memenuhi kebutuhan tugas akademik sekaligus menjadi sarana penyajian informasi mengenai Pimpinan Cabang Muhammadiyah Solo Utara. Informasi yang ditampilkan diharapkan dapat membantu masyarakat mengenal organisasi, kegiatan, dan amal usaha Muhammadiyah di wilayah Solo Utara.

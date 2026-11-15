# Website PCM Solo Utara (Django)

## Menjalankan di VS Code (lokal, SQLite)

Butuh Python 3.14 (lihat `.python-version`) atau jalankan lewat `uv`.

```bash
# 1. Buat virtual env & install dependensi
uv sync                      # atau: python -m venv .venv && pip install django dj-database-url gunicorn pillow "psycopg[binary]" whitenoise

# 2. (Opsional) salin pengaturan lokal
cp .env.local.example .env   # Windows: copy .env.local.example .env

# 3. Siapkan database  <-- WAJIB, kalau dilewati akan error 500
python manage.py migrate
python manage.py seed_pcm    # isi data awal (opsional)
python manage.py createsuperuser

# 4. Jalankan
python manage.py runserver
```

Buka http://127.0.0.1:8000 (admin: http://127.0.0.1:8000/admin/).

## Troubleshooting error 500
- `no such table` -> jalankan `python manage.py migrate`.
- `Missing staticfiles manifest entry` -> `DEBUG=False` di `.env` tanpa `collectstatic`.
  Set `DEBUG=True` untuk lokal, atau jalankan `python manage.py collectstatic`.
- Error koneksi database -> kosongkan `DATABASE_URL` di `.env` untuk memakai SQLite.

## Docker (produksi)
Salin `.env.example` menjadi `.env`, isi `SECRET_KEY`, `POSTGRES_PASSWORD`, dan
`DATABASE_URL=postgres://USER:PASSWORD@db:5432/DBNAME`, lalu `docker compose up --build`.

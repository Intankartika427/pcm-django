from django.db import migrations


TAUTAN_DEFAULT = [
    (
        "LPCR PM PDM SURAKARTA",
        "https://lpcrpmpdmsurakarta.or.id/",
    ),
    (
        "Muhammadiyah Jateng | Gerakan Islam Berkemajuan - Muhammadiyah Jateng",
        "https://muhammadiyahjateng.or.id/",
    ),
    (
        "Instagram",
        "https://www.instagram.com/pcmsolutara/",
    ),
]


def add_default_tautan(apps, schema_editor):
    TautanTerkait = apps.get_model("website", "TautanTerkait")
    database = schema_editor.connection.alias

    for urutan, (nama, url) in enumerate(TAUTAN_DEFAULT, start=1):
        TautanTerkait.objects.using(database).get_or_create(
            nama=nama,
            url=url,
            defaults={"urutan": urutan, "aktif": True},
        )


def remove_default_tautan(apps, schema_editor):
    TautanTerkait = apps.get_model("website", "TautanTerkait")
    database = schema_editor.connection.alias

    for nama, url in TAUTAN_DEFAULT:
        TautanTerkait.objects.using(database).filter(
            nama=nama,
            url=url,
        ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_pesanmasuk"),
    ]

    operations = [
        migrations.RunPython(add_default_tautan, remove_default_tautan),
    ]

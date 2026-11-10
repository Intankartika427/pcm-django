
from django import forms
from .models import PesanMasuk


class PesanMasukForm(forms.ModelForm):
    class Meta:
        model = PesanMasuk

        fields = [
            "nama",
            "email",
            "subjek",
            "pesan",
        ]

        widgets = {
            "nama": forms.TextInput(attrs={
                "placeholder": "Masukkan nama lengkap",
                "style": "width: 80%; padding: 10px; box-sizing: border-box;",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Masukkan alamat email",
                "style": "width: 80%; padding: 10px; box-sizing: border-box;",
            }),
            "subjek": forms.TextInput(attrs={
                "placeholder": "Masukkan subjek pesan",
                "style": "width: 80%; padding: 10px; box-sizing: border-box;",
            }),
            "pesan": forms.Textarea(attrs={
                "placeholder": "Tuliskan pesan Anda",
                "rows": 5,
                "style": "width: 80%; padding: 10px; box-sizing: border-box;",
            }),
        }

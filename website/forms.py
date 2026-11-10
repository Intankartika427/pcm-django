
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
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Masukkan alamat email",
            }),
            "subjek": forms.TextInput(attrs={
                "placeholder": "Masukkan subjek pesan",
            }),
            "pesan": forms.Textarea(attrs={
                "placeholder": "Tuliskan pesan Anda",
                "rows": 5,
            }),
        }

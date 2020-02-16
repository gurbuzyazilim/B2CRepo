from django import forms
from .models import *

class UrunlerForm(forms.ModelForm):

    class Meta:
        model = Urunler
        fields= [
            "Kategori",
            "AltKategori",
            "Marka",
            "Model",
            "Fiyat",
            "Miktar",
            "IlanNo",
            "IlanBasligi",
            "IlanResmi1",
            "IlanResmi2",
            "IlanResmi3",
            "IlanResmi4",
            "IlanResmi5",
            "IlanResmi6",
            "IlanResmi7",
            "IlanResmi8",
            "IlanResmi9",
            "IlanResmi10",
        ]


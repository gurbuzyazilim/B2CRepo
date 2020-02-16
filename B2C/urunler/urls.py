from django.conf.urls import url
from .views import *

app_name = "urunler"

urlpatterns = [
    url(r'^urunekle/$', UrunEkle, name="urunekle"),
    url(r'^sepet/$', SepetGoruntule, name="sepet"),
    url(r'^siparisler/$', Siparisler, name="siparisler"),
    url(r'^tanimlamalar/$', Tanimlamalar, name="tanimlamalar"),
    url(r'^teslimatOdeme/$', TeslimatOdemeOlustur, name="teslimatOdeme"),
    url(r'^(?P<slug>[\w-]+)/$', UrunListele, name="listele"),
    url(r'^(?P<slug>[\w-]+)/detay/$', UrunDetay, name="detay"),
]
from django.conf.urls import url
from .views import *

app_name = "kullanicilar"

urlpatterns = [
    url(r'^giris/$', KullaniciGiris, name="giris"),
    url(r'^kayit/$', KullaniciKayit, name="kayit"),
    url(r'^cikis/$', KullaniciCikis, name="cikis"),
    url(r'^listele/$', KullaniciListele, name="listele"),
    url(r'^tanimlamalar/$', Tanimlamalar, name="tanimlamalar"),
    url(r'^(?P<slug>[\w-]+)/guncelle/$', KullaniciGuncelle, name="guncelle"),
]

from django.conf.urls import url
from .views import *

app_name = "anasayfa"

urlpatterns = [
	url(r'^$', AnaSayfaGoruntule, name='anasayfa'),
	url(r'^tanimlamalar/$', AnaSayfaTanimlama, name='tanimlamalar'),
]
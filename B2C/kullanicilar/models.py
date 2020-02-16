from django.db import models
from django.urls import reverse

class Kullanicilar(models.Model):
	KullaniciAdi    = models.CharField(max_length=50)
	Adi 	        = models.CharField(max_length=50)
	Soyadi 	        = models.CharField(max_length=50)
	Parola          = models.CharField(max_length=50)
	Email           = models.EmailField(max_length=50)
	Tel             = models.CharField(max_length=50)
	Adres           = models.CharField(max_length=200)
	Tipi            = models.CharField(max_length=50,null=True,blank=True)
	Durumu	        = models.BooleanField(default=False)
	SonGiris 	    = models.DateTimeField(null=True)
	KayitTarihi 	= models.DateTimeField(null=True)
	KayitYapan		= models.CharField(max_length=50,null=True)
	DuzeltmeTarihi  = models.DateTimeField(null=True)
	DuzeltmeYapan   = models.CharField(max_length=50,null=True)
	IsSaved 	    = models.BooleanField(default=False)
	IsVerified	    = models.BooleanField(default=False)
	IsActivated	    = models.BooleanField(default=False)
	IsDeleted	    = models.BooleanField(default=False)
	IsCanceled      = models.BooleanField(default=False)
	IsTransferred   = models.BooleanField(default=False)
	IsTransferCache = models.BooleanField(default=False)

	def __str__(self):
		return self.KullaniciAdi

	def get_absolute_url(self):
		return reverse("kullanicilar:guncelle",kwargs={"slug":self.KullaniciAdi})	

class KullaniciTipiModel(models.Model):
	KullaniciTipiKodu  = models.CharField(max_length=10)
	KullaniciTipi      = models.CharField(max_length=50)

"""class ModulYetkileri(models.Model):
	KullaniciTipiKodu  = models.CharField(max_length=10)
	IsAnaSayfa	   = models.BooleanField(default=True)
	IsCari		   = models.BooleanField(default=False)
	IsKasa		   = models.BooleanField(default=False)
	IsBanka	       = models.BooleanField(default=False)
	IsCekSenet	   = models.BooleanField(default=False)
	IsSiparis      = models.BooleanField(default=False)
	IsFatura       = models.BooleanField(default=False)
	IsIrsaliye     = models.BooleanField(default=False)
	IsStok 		   = models.BooleanField(default=False)
	IsKullanicilar = models.BooleanField(default=False)
	IsTanimlamalar = models.BooleanField(default=False)

class KullaniciYetkileri(models.Model):
	KullaniciTipiKodu 	= models.CharField(max_length=10)
	IsKullaniciOlustur  = models.BooleanField(default=False)
	IsKullaniciListele  = models.BooleanField(default=False)
	IsKullaniciDetay    = models.BooleanField(default=False)
	IsKullaniciGuncelle = models.BooleanField(default=False)
	IsKullaniciSil      = models.BooleanField(default=False)"""
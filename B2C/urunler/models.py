from django.db import models

class Urunler(models.Model):
	Kategori    = models.CharField(max_length=50)
	AltKategori = models.CharField(max_length=50)
	Marka       = models.CharField(max_length=50)
	Model       = models.CharField(max_length=50)
	IlanNo      = models.CharField(max_length=50)
	IlanBasligi = models.CharField(max_length=50)
	Fiyat       = models.DecimalField(max_digits=20,decimal_places=2)
	Miktar      = models.IntegerField()
	IlanResmi1  = models.ImageField(null=True,blank=True)
	IlanResmi2  = models.ImageField(null=True,blank=True)
	IlanResmi3  = models.ImageField(null=True,blank=True)
	IlanResmi4  = models.ImageField(null=True,blank=True)
	IlanResmi5  = models.ImageField(null=True,blank=True)
	IlanResmi6  = models.ImageField(null=True,blank=True)
	IlanResmi7  = models.ImageField(null=True,blank=True)
	IlanResmi8  = models.ImageField(null=True,blank=True)
	IlanResmi9  = models.ImageField(null=True,blank=True)
	IlanResmi10 = models.ImageField(null=True,blank=True)

class UrunTanimlamalari(models.Model):
	Kodu    = models.CharField(max_length=10)
	Icerik  = models.CharField(max_length=50)
	UstKodu = models.CharField(max_length=10,null=True,blank=True)

class UrunOzellikleri(models.Model):
	IlanNo       = models.CharField(max_length=10)
	UrunOzBaslik = models.CharField(max_length=50)
	UrunOzellik  = models.CharField(max_length=100)

class Yorumlar(models.Model):
	Yorum   = models.CharField(max_length=250)
	Isim    = models.CharField(max_length=50)
	Soyisim = models.CharField(max_length=50)
	Email   = models.EmailField()

class Sepet(models.Model):
	KullaniciAdi = models.CharField(max_length=10)
	IlanNo       = models.CharField(max_length=20)
	Miktar       = models.IntegerField(null=True)
	IsSaved 	 = models.BooleanField(default=False)
	IsVerified	 = models.BooleanField(default=False)
	IsDeleted	 = models.BooleanField(default=False)
	IsCanceled   = models.BooleanField(default=False)

class TeslimatOdeme(models.Model):
	KullaniciAdi = models.CharField(max_length=10)
	Isim         = models.CharField(max_length=20)
	Soyisim      = models.CharField(max_length=20)
	Tel          = models.CharField(max_length=20)
	Email        = models.EmailField()
	Adres        = models.CharField(max_length=200)
	OdemeTipi    = models.CharField(max_length=20)
	IsSaved 	 = models.BooleanField(default=False)
	IsVerified	 = models.BooleanField(default=False)
	IsDeleted	 = models.BooleanField(default=False)
	IsCanceled   = models.BooleanField(default=False)

class Siparis(models.Model):
	KullaniciAdi = models.CharField(max_length=10)
	SiparisNo    = models.CharField(max_length=20)
	IsSaved 	 = models.BooleanField(default=False)
	IsVerified	 = models.BooleanField(default=False)
	IsDeleted	 = models.BooleanField(default=False)
	IsCanceled   = models.BooleanField(default=False)	

class Manset(models.Model):
	IlanNo      = models.CharField(max_length=50)
	IlanBasligi = models.CharField(max_length=50)
	MansetResmi = models.ImageField()

class Vitrin(models.Model):
	IlanNo      = models.CharField(max_length=50)
	IlanBasligi = models.CharField(max_length=50)
	VitrinResmi = models.ImageField()	
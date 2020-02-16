import random
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .encryption import encryption_h
from django.utils import timezone

def Capce():
	liste = range(10)
	capce = ""
	for i in random.sample(liste, 5):
		capce = capce + str(i)
	return capce	
	
def KullaniciGiris(request):
	request.session.clear()
	if request.is_ajax():
		ajaxKullaniciAdi    = request.POST.get("ajaxKullaniciAdi")
		ajaxKullaniciParola = request.POST.get("ajaxKullaniciParola")
		ajaxCapce 			= request.POST.get("ajaxCapce")
		if(ajaxCapce == capce):
			if (ajaxKullaniciAdi != "" and ajaxKullaniciParola != ""):
				encryptionParola = encryption_h(ajaxKullaniciAdi, ajaxKullaniciParola)
				try:
					sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciAdi=ajaxKullaniciAdi, Parola=encryptionParola)
					if(sqlKullanicilar.Durumu == True):
						sqlKullanicilar.SonGiris    = timezone.now()
						sqlKullanicilar.IsActivated = True
						sqlKullanicilar.save()
						request.session["KullaniciAdi"] = sqlKullanicilar.KullaniciAdi
						ajaxMesaj = True
					if(sqlKullanicilar.Durumu == False):
						ajaxMesaj = "Pasif Kullanıcı ! Site Yöneticisiyle Görüşün."	
				except:
					ajaxMesaj = "Böyle Bir Kullanici Yok !"	
			else:
				ajaxMesaj = "Kullanıcı Adı Ve Parola Boş Bırakılamaz !"
		else:
			ajaxMesaj = "Girmiş Olduğunuz Kod Doğrulanamadı !"
		context = {"ajaxMesaj" : ajaxMesaj}
		return JsonResponse(context)
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	global capce	
	capce = Capce()
	context = {
		"key"   : key,
		"capce" : capce,
	}
	return render(request, "kullanicilar/giris.html", context)

def KullaniciCikis(request):
	try:
		sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciAdi=request.session["KullaniciAdi"])
		sqlKullanicilar.IsActivated = False
		sqlKullanicilar.save()
	except:
		pass		
	request.session.clear()
	return redirect ("anasayfa:anasayfa")

def KullaniciKayit(request):
	if request.is_ajax():
		ajaxKullaniciAdi = request.POST.get("ajaxKullaniciAdi")
		ajaxAdi 		 = request.POST.get("ajaxAdi")
		ajaxSoyadi       = request.POST.get("ajaxSoyadi")
		ajaxParola       = request.POST.get("ajaxParola")
		ajaxParolaD      = request.POST.get("ajaxParolaD")
		ajaxEmail        = request.POST.get("ajaxEmail")
		ajaxTel          = request.POST.get("ajaxTel")
		ajaxAdres        = request.POST.get("ajaxAdres")
		if(ajaxKullaniciAdi and ajaxAdi and ajaxSoyadi and ajaxEmail and ajaxTel and ajaxAdres and ajaxParola and ajaxParolaD):	
			if(ajaxParola == ajaxParolaD):
				try:
					sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciAdi=ajaxKullaniciAdi)
					ajaxMesaj = "Kayıtlı Kullanıcı Adı !"
					key1 = 0
				except:
					key1 = 1	
				if(key1 == 1):
					encryptionParola = encryption_h(ajaxKullaniciAdi, ajaxParola)
					sqlKullanicilarKayit = Kullanicilar()
					sqlKullanicilarKayit.KullaniciAdi = ajaxKullaniciAdi
					sqlKullanicilarKayit.Adi          = ajaxAdi
					sqlKullanicilarKayit.Soyadi       = ajaxSoyadi
					sqlKullanicilarKayit.Parola       = encryptionParola
					sqlKullanicilarKayit.Email        = ajaxEmail
					sqlKullanicilarKayit.Tel          = ajaxTel
					sqlKullanicilarKayit.Adres        = ajaxAdres
					sqlKullanicilarKayit.KayitTarihi  = timezone.now()
					sqlKullanicilarKayit.KayitYapan   = ajaxKullaniciAdi
					sqlKullanicilarKayit.save()
					ajaxMesaj = "Kayıt Başarılı !"
			else:
				ajaxMesaj = "Parolalar Eşleşmiyor !"
			context = {"ajaxMesaj" : ajaxMesaj}
			return JsonResponse(context)
		else:
			ajaxMesaj = "Lütfen Formu Boş Bırakmayınız !"
			context = {"ajaxMesaj" : ajaxMesaj}
			return JsonResponse(context)		
	sqlKullaniciTipiModel = KullaniciTipiModel.objects.all()			
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                   : key,
		"sqlKullaniciTipiModel" : sqlKullaniciTipiModel,
	}
	return render(request, "kullanicilar/kayit.html",context)

def KullaniciGuncelle(request,slug):
	if request.is_ajax():
		ajaxKullaniciAdi = request.POST.get("ajaxKullaniciAdi")
		ajaxAdi 		 = request.POST.get("ajaxAdi")
		ajaxSoyadi       = request.POST.get("ajaxSoyadi")
		ajaxParola       = request.POST.get("ajaxParola")
		ajaxParolaD      = request.POST.get("ajaxParolaD")
		ajaxEmail        = request.POST.get("ajaxEmail")
		ajaxTel          = request.POST.get("ajaxTel")
		ajaxAdres        = request.POST.get("ajaxAdres")
		if(ajaxKullaniciAdi and ajaxAdi and ajaxSoyadi and ajaxTel and ajaxAdres and ajaxParola and ajaxParolaD):	
			if(ajaxParola == ajaxParolaD):	
				encryptionParola = encryption_h(ajaxKullaniciAdi, ajaxParola)
				sqlKullanicilarGuncelle = get_object_or_404(Kullanicilar, KullaniciAdi=request.session["KullaniciAdi"])
				sqlKullanicilarGuncelle.KullaniciAdi   = ajaxKullaniciAdi
				sqlKullanicilarGuncelle.Adi            = ajaxAdi
				sqlKullanicilarGuncelle.Soyadi         = ajaxSoyadi
				sqlKullanicilarGuncelle.Parola         = encryptionParola
				sqlKullanicilarGuncelle.Email          = ajaxEmail
				sqlKullanicilarGuncelle.Tel            = ajaxTel
				sqlKullanicilarGuncelle.Adres          = ajaxAdres
				sqlKullanicilarGuncelle.DuzeltmeTarihi = timezone.now()
				sqlKullanicilarGuncelle.DuzeltmeYapan  = request.session["KullaniciAdi"]
				sqlKullanicilarGuncelle.save()
				ajaxMesaj = True
			else:
				ajaxMesaj = "Parolalar Eşleşmiyor !"
			context = {"ajaxMesaj" : ajaxMesaj}
			return JsonResponse(context)
		else:
			context = {"ajaxMesaj" : "Lütfen Formu Boş Bırakmayınız !"}
			return JsonResponse(context)
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False			
	context = {"key" : key}
	return render(request, "kullanicilar/guncelle.html",context)

def KullaniciListele(request):
	if request.is_ajax():
		ajaxDetay = request.POST.get("ajaxDetay")
		if(ajaxDetay):
			sqlKullanicilarDetay = get_object_or_404(Kullanicilar,KullaniciAdi=ajaxDetay)
			context = {
				"ajaxKullaniciAdi"   : sqlKullanicilarDetay.KullaniciAdi,
				"ajaxAdi"            : sqlKullanicilarDetay.Adi,
				"ajaxSoyadi"         : sqlKullanicilarDetay.Soyadi,
				"ajaxEmail"          : sqlKullanicilarDetay.Email,
				"ajaxTel"            : sqlKullanicilarDetay.Tel,
				"ajaxAdres"          : sqlKullanicilarDetay.Adres,
				"ajaxTipi"           : sqlKullanicilarDetay.Tipi,
				"ajaxDurumu"         : sqlKullanicilarDetay.Durumu,
				"ajaxSonGiris"       : sqlKullanicilarDetay.SonGiris,
				"ajaxKayitTarihi"    : sqlKullanicilarDetay.KayitTarihi,
				"ajaxKayitYapan"     : sqlKullanicilarDetay.KayitYapan,
				"ajaxDuzeltmeTarihi" : sqlKullanicilarDetay.DuzeltmeTarihi,
				"ajaxDuzeltmeYapan"  : sqlKullanicilarDetay.DuzeltmeYapan,
			}
			return JsonResponse(context)
		ajaxGuncelle = request.POST.get("ajaxGuncelle")
		if(ajaxGuncelle):
			sqlKullanicilarGuncelle = get_object_or_404(Kullanicilar,KullaniciAdi=ajaxGuncelle)
			if(sqlKullanicilarGuncelle.Durumu == True):
				varKullaniciDurumu = 1
			if(sqlKullanicilarGuncelle.Durumu == False):
				varKullaniciDurumu = 0	
			context = {
				"ajaxIdGuncelle"     : sqlKullanicilarGuncelle.id,
				"ajaxTipiGuncelle"   : sqlKullanicilarGuncelle.Tipi,
				"ajaxDurumuGuncelle" : varKullaniciDurumu,
			}
			return JsonResponse(context)
			
		ajaxIdKaydet     = request.POST.get("ajaxIdKaydet")
		ajaxTipiKaydet   = request.POST.get("ajaxTipiKaydet")
		ajaxDurumuKaydet = request.POST.get("ajaxDurumuKaydet")
		if(ajaxIdKaydet):
			if(ajaxTipiKaydet and ajaxDurumuKaydet):
				sqlKaydet = get_object_or_404(Kullanicilar,id=ajaxIdKaydet)
				sqlKaydet.Tipi           = ajaxTipiKaydet
				sqlKaydet.Durumu         = ajaxDurumuKaydet
				sqlKaydet.DuzeltmeTarihi = timezone.now()
				sqlKaydet.DuzeltmeYapan  = request.session["KullaniciAdi"]
				sqlKaydet.save()
				ajaxMesaj = "Kayıt Başarılı Bir Şekilde Güncellendi !"
				context = {"ajaxMesaj" : ajaxMesaj}
				return JsonResponse(context)
			else:
				ajaxMesaj = "Lütfen Formu Boş Bırakmayınız !"
				context = {"ajaxMesaj" : ajaxMesaj}
				return JsonResponse(context)	
		ajaxSil = request.POST.get("ajaxSil")
		if(ajaxSil):
			sqlKullanicilarSil = get_object_or_404(Kullanicilar,KullaniciAdi=ajaxSil)
			sqlKullanicilarSil.IsDeleted = True
			sqlKullanicilarSil.save()
			context = {"ajaxMesaj" : "Silme İşlemi Başarılı !",}
			return JsonResponse(context)				
	sqlKullanicilarListesi = Kullanicilar.objects.filter(IsDeleted=False)
	sqlKullaniciTipi = KullaniciTipiModel.objects.all()
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                    : key,
		"sqlKullanicilarListesi" : sqlKullanicilarListesi,
		"sqlKullaniciTipi"       : sqlKullaniciTipi,
	}
	return render (request, "kullanicilar/listele.html", context)

def Tanimlamalar(request):		
	if request.is_ajax():
		ajaxKullaniciTipiKodu  = request.POST.get("ajaxKullaniciTipiKodu")
		ajaxKullaniciTipi      = request.POST.get("ajaxKullaniciTipi")
		if(ajaxKullaniciTipi):
			sqlKullaniciTanimlamalari = KullaniciTipiModel()
			sqlKullaniciTanimlamalari.KullaniciTipiKodu = ajaxKullaniciTipiKodu
			sqlKullaniciTanimlamalari.KullaniciTipi     = ajaxKullaniciTipi
			sqlKullaniciTanimlamalari.save()
			context = {"ajaxMesaj" : "Kayıt Başarılı !",}
			return JsonResponse(context)
		
	varKullaniciTipiModel = KullaniciTipiModel.objects.all()
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                   : key,
		"varKullaniciTipiModel" : varKullaniciTipiModel,
	}		
	return render (request, "kullanicilar/tanimlamalar.html", context)
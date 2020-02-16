from kullanicilar.models import *
from kullanicilar.views import Capce
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404,Http404, redirect
from django.http import JsonResponse

def UrunEkle(request):
	if request.is_ajax():
		ajaxKategori = request.POST.get("ajaxKategori")	
		if(ajaxKategori):
			altKategoriListesi = []
			for altKategori in UrunTanimlamalari.objects.values_list().filter(UstKodu=ajaxKategori):
				altKategoriListesi.append(altKategori)	
			context = {"ajaxAltKategoriListesi" : altKategoriListesi}
			return JsonResponse(context)
		ajaxAltKategori = request.POST.get("ajaxAltKategori")	
		if(ajaxAltKategori):
			markaListesi = []
			for marka in UrunTanimlamalari.objects.values_list().filter(UstKodu=ajaxAltKategori):
				markaListesi.append(marka)
			context = {"ajaxMarkaListesi" : markaListesi}
			return JsonResponse(context)
		ajaxMarka = request.POST.get("ajaxMarka")	
		if(ajaxMarka):
			modelListesi = []
			for model in UrunTanimlamalari.objects.values_list().filter(UstKodu=ajaxMarka):
				modelListesi.append(model)
			context = {"ajaxModelListesi" : modelListesi}
			return JsonResponse(context)


		ajaxIlanNo   = request.POST.get("ajaxIlanNo")
		ajaxOzBaslik = request.POST.get("ajaxOzBaslik")
		ajaxOzellik  = request.POST.get("ajaxOzellik")
		if(ajaxIlanNo):	
			sqlUrunOzellikleri = UrunOzellikleri()
			sqlUrunOzellikleri.IlanNo       = ajaxIlanNo
			sqlUrunOzellikleri.UrunOzBaslik = ajaxOzBaslik
			sqlUrunOzellikleri.UrunOzellik  = ajaxOzellik
			sqlUrunOzellikleri.save()
			context = {
				"ajaxOzBaslik" : sqlUrunOzellikleri.UrunOzBaslik,
				"ajaxOzellik"  : sqlUrunOzellikleri.UrunOzellik,
			}
			return JsonResponse(context)


	sqlUrunlerForm = UrunlerForm(request.POST or None, request.FILES or None)
	modelRedirect = request.POST.get("Model")
	if sqlUrunlerForm.is_valid():
		sqlUrunlerForm.save()
		return redirect("/urunler/"+modelRedirect+"")
	sqlUrunTanimlamalari = UrunTanimlamalari.objects.filter(UstKodu="")
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                  : key,
		"sqlUrunlerForm"       : sqlUrunlerForm,
		"sqlUrunTanimlamalari" : sqlUrunTanimlamalari,
	}
	return render(request,"urunler/urunEkle.html",context)

def Tanimlamalar(request):
	if request.is_ajax():
		ajaxKodu    = request.POST.get("ajaxKodu")
		ajaxIcerik  = request.POST.get("ajaxIcerik")
		ajaxUstKodu = request.POST.get("ajaxUstKodu")
		if(ajaxKodu):
			sqlUrunTanimlamalari = UrunTanimlamalari()
			sqlUrunTanimlamalari.Kodu    = ajaxKodu
			sqlUrunTanimlamalari.Icerik  = ajaxIcerik
			sqlUrunTanimlamalari.UstKodu = ajaxUstKodu
			sqlUrunTanimlamalari.save()
			context = {"ajaxMesaj" : "Tanimlama Eklendi !"}
			return JsonResponse(context)
		
	sqlUrunTanimlamalari = UrunTanimlamalari.objects.all()
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                  : key,
		"sqlUrunTanimlamalari" : sqlUrunTanimlamalari,
	}
	return render(request,"urunler/tanimlamalar.html",context)	

def UrunListele(request,slug):
	sqlUrunler = Urunler.objects.filter(Model=slug)
	if(sqlUrunler.exists()):
		try:
			key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
		except:
			key = False
		context = {
			"key"        : key,
			"sqlUrunler" : sqlUrunler,
		}
		return render(request,"urunler/listele.html",context)
	else:
		raise Http404()
					
def UrunDetay(request,slug):
	if request.is_ajax():
		ajaxYorum   = request.POST.get("ajaxYorum")
		ajaxIsim    = request.POST.get("ajaxIsim")
		ajaxSoyisim = request.POST.get("ajaxSoyisim")
		ajaxEmail   = request.POST.get("ajaxEmail")
		if(ajaxYorum):
			sqlYorumlar = Yorumlar()
			sqlYorumlar.Yorum   = ajaxYorum
			sqlYorumlar.Isim    = ajaxIsim
			sqlYorumlar.Soyisim = ajaxSoyisim
			sqlYorumlar.Email   = ajaxEmail
			sqlYorumlar.save()
			context = {"ajaxMesaj" : "Başarılı"}
			return JsonResponse(context)
		ajaxSepetEkle = request.POST.get("ajaxSepetEkle")
		ajaxMiktar    = request.POST.get("ajaxMiktar")
		if(ajaxSepetEkle):
			sqlUrunlerMiktar = get_object_or_404(Urunler,IlanNo=ajaxSepetEkle)
			if(sqlUrunlerMiktar.Miktar == 0):
				key = False
			else:
				sqlSepetEkle = Sepet()
				sqlSepetEkle.IlanNo       = ajaxSepetEkle
				sqlSepetEkle.Miktar       = ajaxMiktar
				sqlSepetEkle.KullaniciAdi = request.session["KullaniciAdi"]
				sqlSepetEkle.save()
				sqlUrunlerMiktar.Miktar = sqlUrunlerMiktar.Miktar - int(ajaxMiktar)
				sqlUrunlerMiktar.save()
				key = True
			context = {"ajaxMesaj" : key,}
			return JsonResponse(context)
		
	resimListesi = []
	sqlUrun            = get_object_or_404(Urunler,IlanNo=slug)
	if(sqlUrun.IlanResmi1 != ""):
		resimListesi.append(sqlUrun.IlanResmi1.url)
	if(sqlUrun.IlanResmi2 != ""):
		resimListesi.append(sqlUrun.IlanResmi2.url)
	if(sqlUrun.IlanResmi3 != ""):
		resimListesi.append(sqlUrun.IlanResmi3.url)
	if(sqlUrun.IlanResmi4 != ""):
		resimListesi.append(sqlUrun.IlanResmi4.url)
	if(sqlUrun.IlanResmi5 != ""):
		resimListesi.append(sqlUrun.IlanResmi5.url)
	if(sqlUrun.IlanResmi6 != ""):
		resimListesi.append(sqlUrun.IlanResmi6.url)
	if(sqlUrun.IlanResmi7 != ""):
		resimListesi.append(sqlUrun.IlanResmi7.url)
	if(sqlUrun.IlanResmi8 != ""):
		resimListesi.append(sqlUrun.IlanResmi8.url)
	if(sqlUrun.IlanResmi9 != ""):
		resimListesi.append(sqlUrun.IlanResmi9.url)
	if(sqlUrun.IlanResmi10 != ""):
		resimListesi.append(sqlUrun.IlanResmi10.url)										
	sqlUrunOzellikleri = UrunOzellikleri.objects.filter(IlanNo=slug)
	sqlYorumlar = Yorumlar.objects.all()
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"                : key,
		"resimListesi"       : resimListesi,
		"sqlUrun"            : sqlUrun,
		"sqlUrunOzellikleri" : sqlUrunOzellikleri,
		"sqlYorumlar"        : sqlYorumlar,
		}
	return render(request,"urunler/detay.html",context)

def SepetGoruntule(request):
	if request.is_ajax():	
		ajaxSil = request.POST.get("ajaxSil")	
		if(ajaxSil):
			sqlSepetUrunSil = get_object_or_404(Sepet,KullaniciAdi=request.session["KullaniciAdi"],IlanNo=ajaxSil)
			sqlSepetUrunSil.delete()
			sqlUrunlerMikIade = get_object_or_404(Urunler,IlanNo=ajaxSil)
			sqlUrunlerMikIade.Miktar = sqlUrunlerMikIade.Miktar + sqlSepetUrunSil.Miktar
			sqlUrunlerMikIade.save()
			toplamTutar = 0
			for sepet in Sepet.objects.filter(KullaniciAdi=request.session["KullaniciAdi"]):
				sqlUrunler = get_object_or_404(Urunler,IlanNo=sepet.IlanNo)
				toplamTutar = toplamTutar + sqlUrunler.Fiyat
			context = {
				"ajaxMesaj"  : ajaxSil,
				"ajaxTopTut" : toplamTutar,
			}
			return JsonResponse(context)
	try:
		sepetListesi = []
		toplamTutar = 0
		for sepet in Sepet.objects.filter(KullaniciAdi=request.session["KullaniciAdi"],IsSaved=False):
			sqlUrunler = get_object_or_404(Urunler,IlanNo=sepet.IlanNo)
			sepetUrun = [sqlUrunler.IlanNo,sqlUrunler.IlanBasligi,sqlUrunler.IlanResmi1.url,sqlUrunler.Fiyat]
			sepetListesi.append(sepetUrun)
			toplamTutar = toplamTutar + sqlUrunler.Fiyat
		if sepetListesi:
			key1 = 1
		else:
			key1 = 0
	except:
		key1 = 0
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False	
	context = {
		"key"          : key,
		"key1"         : key1,
		"sepetListesi" : sepetListesi,
		"toplamTutar"  : toplamTutar,
	}
	return render(request,"urunler/sepet.html",context)	

def TeslimatOdemeOlustur(request):
	if request.is_ajax():
		ajaxVeri      = request.POST.get("ajaxVeri")
		if(ajaxVeri):
			sepettekiUrunler = []
			toplamTutar = 0
			for sepet in Sepet.objects.filter(KullaniciAdi=request.session["KullaniciAdi"]):
				sqlSepetUrunler = get_object_or_404(Urunler,IlanNo=sepet.IlanNo)
				sepetUrun = [sqlSepetUrunler.Marka,sqlSepetUrunler.Model,sqlSepetUrunler.IlanBasligi,\
				sqlSepetUrunler.Fiyat]
				sepettekiUrunler.append(sepetUrun)
				toplamTutar = toplamTutar + sqlSepetUrunler.Fiyat
			context = {
				"ajaxSepettekiUrunler" : sepettekiUrunler,
				"ajaxToplamTutar"      : str(toplamTutar),
			}
			return JsonResponse(context)
			
		ajaxIsim      = request.POST.get("ajaxIsim")
		ajaxSoyisim   = request.POST.get("ajaxSoyisim")
		ajaxTelefon   = request.POST.get("ajaxTelefon")
		ajaxEmail     = request.POST.get("ajaxEmail")
		ajaxAdres     = request.POST.get("ajaxAdres")
		ajaxOdemeTipi = request.POST.get("ajaxOdemeTipi")
		if(ajaxIsim):
			try:
				sqlTesOdGunc = get_object_or_404(TeslimatOdeme,KullaniciAdi=request.session["KullaniciAdi"])
				sqlTesOdGunc.Isim         = ajaxIsim
				sqlTesOdGunc.Soyisim      = ajaxSoyisim
				sqlTesOdGunc.Tel          = ajaxTelefon
				sqlTesOdGunc.Email        = ajaxEmail
				sqlTesOdGunc.Adres        = ajaxAdres
				sqlTesOdGunc.OdemeTipi    = ajaxOdemeTipi
				sqlTesOdGunc.KullaniciAdi = request.session["KullaniciAdi"]
				sqlTesOdGunc.save()
			except:
				sqlTeslimatOdeme = TeslimatOdeme()
				sqlTeslimatOdeme.Isim         = ajaxIsim
				sqlTeslimatOdeme.Soyisim      = ajaxSoyisim
				sqlTeslimatOdeme.Tel          = ajaxTelefon
				sqlTeslimatOdeme.Email        = ajaxEmail
				sqlTeslimatOdeme.Adres        = ajaxAdres
				sqlTeslimatOdeme.OdemeTipi    = ajaxOdemeTipi
				sqlTeslimatOdeme.KullaniciAdi = request.session["KullaniciAdi"]
				sqlTeslimatOdeme.save()

			sqlSiparis = Siparis()
			sqlSiparis.KullaniciAdi = request.session["KullaniciAdi"]
			sqlSiparis.SiparisNo    = "SIP"+Capce()
			sqlSiparis.save()
			
			for sepetIsSaved in Sepet.objects.filter(KullaniciAdi=request.session["KullaniciAdi"]):
				sepetIsSaved.IsSaved = True
				sepetIsSaved.save()

			context = {
				"ajaxMesaj"    : "Siparişiniz Başarılı Bir Şekilde Alındı !",
				"ajaxLocation" : "/anasayfa",
			}
			return JsonResponse(context)
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False		
	context = {"key" : key}
	return render(request,"urunler/teslimatOdeme.html",context)


def Siparisler(request):
	if request.is_ajax():
		ajaxIptal = request.POST.get("ajaxIptal")
		if(ajaxIptal):
			sqlSiparis = get_object_or_404(Siparis,SiparisNo=ajaxIptal)
			sqlSiparis.IsCanceled = True
			sqlSiparis.save()
			context = {"ajaxMesaj" : "Siparis Silindi"}
			return JsonResponse(context)
		ajaxOnayla = request.POST.get("ajaxOnayla")
		if(ajaxOnayla):
			sqlSiparis = get_object_or_404(Siparis,SiparisNo=ajaxOnayla)
			sqlSiparis.IsVerified = True
			sqlSiparis.save()
			context = {"ajaxMesaj" : "Siparis Onaylandı"}
			return JsonResponse(context)	
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"        : key,
		"sqlSiparis" : Siparis.objects.all(),
	}
	return render(request,"urunler/siparisler.html",context)		

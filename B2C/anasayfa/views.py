import random
from kullanicilar.models import *
from urunler.models import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def AnaSayfaGoruntule(request):
	try:
		request.session["KullaniciAdi"] != None
	except:
		liste = range(10)	
		capce = ""
		for i in random.sample(liste, 5):
			capce = capce + str(i)
		request.session["KullaniciAdi"] = capce
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
	sqlTanimlamalar = UrunTanimlamalari.objects.filter(UstKodu="")
	mansetResimleri = Manset.objects.all()
	vitrinResimleri = Vitrin.objects.all()
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key"             : key,
		"sqlTanimlamalar" : sqlTanimlamalar,
		"mansetResimleri" : mansetResimleri,
		"vitrinResimleri" : vitrinResimleri,
	}
	return render(request,"anasayfa/anasayfa.html", context)

def AnaSayfaTanimlama(request):
	if request.is_ajax():
		ajaxMRINo = request.POST.get("ajaxMRINo")	
		if(ajaxMRINo):
			resimListesi = []
			sqlUrun = get_object_or_404(Urunler,IlanNo=ajaxMRINo)
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
			context = {
				"ajaxResimListesi" : resimListesi,
				"ajaxIlanNo"       : sqlUrun.IlanNo,
			}
			return JsonResponse(context)
		
		ajaxManIlNo  = request.POST.get("ajaxManIlNo")
		ajaxManRes   = request.POST.get("ajaxManRes")
		if(ajaxManRes):
			sqlManBas = get_object_or_404(Urunler,IlanNo=ajaxManIlNo)
			sqlManset = Manset()
			sqlManset.IlanNo      = ajaxManIlNo
			sqlManset.IlanBasligi = sqlManBas.IlanBasligi
			sqlManset.MansetResmi = ajaxManRes
			sqlManset.save()
			context = {"ajaxMesaj" : "Başarılı"}
			return JsonResponse(context)

		ajaxVitIlNo  = request.POST.get("ajaxVitIlNo")
		ajaxVitRes   = request.POST.get("ajaxVitRes")
		if(ajaxVitRes):
			sqlVitBas = get_object_or_404(Urunler,IlanNo=ajaxVitIlNo)
			sqlVitrin = Vitrin()
			sqlVitrin.IlanNo      = ajaxVitIlNo
			sqlVitrin.IlanBasligi = sqlVitBas.IlanBasligi
			sqlVitrin.VitrinResmi = ajaxVitRes
			sqlVitrin.save()
			context = {"ajaxMesaj" : "Başarılı"}
			return JsonResponse(context)
	try:
		key = get_object_or_404(Kullanicilar,KullaniciAdi=request.session["KullaniciAdi"])
	except:
		key = False
	context = {
		"key" : key,
	}
	return render(request,"anasayfa/tanimlamalar.html",context)	
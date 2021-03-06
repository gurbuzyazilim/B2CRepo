# Generated by Django 2.2.10 on 2020-02-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kullanicilar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KullaniciAdi', models.CharField(max_length=50)),
                ('Adi', models.CharField(max_length=50)),
                ('Soyadi', models.CharField(max_length=50)),
                ('Parola', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Tel', models.CharField(max_length=50)),
                ('Adres', models.CharField(max_length=200)),
                ('Tipi', models.CharField(blank=True, max_length=50, null=True)),
                ('Durumu', models.BooleanField(default=False)),
                ('SonGiris', models.DateTimeField(null=True)),
                ('KayitTarihi', models.DateTimeField(null=True)),
                ('KayitYapan', models.CharField(max_length=50, null=True)),
                ('DuzeltmeTarihi', models.DateTimeField(null=True)),
                ('DuzeltmeYapan', models.CharField(max_length=50, null=True)),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsActivated', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KullaniciTipiModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KullaniciTipiKodu', models.CharField(max_length=10)),
                ('KullaniciTipi', models.CharField(max_length=50)),
            ],
        ),
    ]

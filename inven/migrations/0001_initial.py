# Generated by Django 2.2.24 on 2021-06-28 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('merk', models.CharField(blank=True, max_length=100, null=True)),
                ('kode', models.CharField(max_length=20, null=True)),
                ('tahun_perolehan', models.PositiveIntegerField(null=True)),
                ('penguasaan', models.CharField(max_length=50)),
                ('keterangan', models.CharField(blank=True, default='-', max_length=250, null=True)),
                ('Foto', models.FileField(blank=True, default='barang.jpg', null=True, upload_to='')),
                ('status', models.CharField(default='Tersedia', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('nip', models.CharField(max_length=250, unique=True)),
                ('pangkat_atau_golongan', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=250)),
                ('Foto', models.FileField(blank=True, default='karyawan.jpg', null=True, upload_to='')),
                ('tanggal_terdaftar', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='peminjaman_barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_pinjam', models.CharField(max_length=100, null=True)),
                ('status_peminjaman', models.CharField(default='Dipinjam', max_length=100)),
                ('tanggal_pinjam', models.DateField(auto_now_add=True)),
                ('barang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inven.barang')),
                ('pegawai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inven.pegawai')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pengembalian_barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_kembali', models.DateField(auto_now_add=True)),
                ('peminjaman_barang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inven.peminjaman_barang')),
            ],
        ),
        migrations.CreateModel(
            name='keranjang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inven.barang')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

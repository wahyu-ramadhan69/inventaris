# Generated by Django 2.2.19 on 2021-05-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inven', '0007_peminjaman_barang_nama_op'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengembalian_barang',
            name='id_op',
        ),
        migrations.AlterField(
            model_name='peminjaman_barang',
            name='nama_op',
            field=models.CharField(max_length=100),
        ),
    ]

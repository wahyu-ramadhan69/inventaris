# Generated by Django 2.2.19 on 2021-05-25 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inven', '0008_auto_20210525_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengembalian_barang',
            name='nama_op',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

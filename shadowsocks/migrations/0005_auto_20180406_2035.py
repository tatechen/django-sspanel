# Generated by Django 2.0 on 2018-04-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0004_shop_sale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['level'], 'verbose_name_plural': '商品'},
        ),
    ]

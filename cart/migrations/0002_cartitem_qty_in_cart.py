# Generated by Django 4.1.4 on 2023-03-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='qty_in_cart',
            field=models.IntegerField(default=1),
        ),
    ]
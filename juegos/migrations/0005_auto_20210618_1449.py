# Generated by Django 3.1.5 on 2021-06-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0004_juego_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
# Generated by Django 3.1.5 on 2021-06-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0003_auto_20210618_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]

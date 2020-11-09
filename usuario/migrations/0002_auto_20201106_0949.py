# Generated by Django 3.1.2 on 2020-11-06 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='nrTarjeta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='tiempo',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
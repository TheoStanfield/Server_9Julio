# Generated by Django 3.1.1 on 2020-12-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20201118_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deuda', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='NoSocio',
        ),
    ]

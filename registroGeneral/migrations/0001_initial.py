# Generated by Django 3.1.4 on 2020-12-09 14:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=30)),
                ('tiempo', models.DateTimeField(default=django.utils.timezone.now)),
                ('entra', models.BooleanField(default=True)),
                ('sale', models.BooleanField(default=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.persona')),
            ],
        ),
    ]

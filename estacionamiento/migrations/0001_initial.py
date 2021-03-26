# Generated by Django 3.1.7 on 2021-03-25 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0002_auto_20210323_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='CicloAnual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cicloAnual', models.IntegerField(verbose_name='cicloAnual')),
            ],
        ),
        migrations.CreateModel(
            name='CicloCaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cicloCaja', models.IntegerField(verbose_name='cicloCaja')),
                ('recaudado', models.IntegerField(blank=True, null=True, verbose_name='recaudado')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProveedor', models.CharField(max_length=30, verbose_name='idProveedor')),
                ('nombre_proveedor', models.CharField(max_length=30, verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEstacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('socio', 'SOCIO'), ('socio-moroso', 'SOCIO-MOROSO'), ('nosocio', 'NOSOCIO'), ('proveedor', 'PROVEEDOR')], default='SOCIO', max_length=30, verbose_name='Tipo')),
                ('identificador', models.CharField(blank=True, default='Error', max_length=30, null=True, verbose_name='Identificador')),
                ('noSocio', models.IntegerField(blank=True, null=True, verbose_name='DNI')),
                ('lugar', models.CharField(max_length=30, verbose_name='Lugar')),
                ('tiempo', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y Hora')),
                ('direccion', models.CharField(choices=[('entrada', 'ENTRADA'), ('salida', 'SALIDA')], default='ENTRADA', max_length=30, verbose_name='Dirección')),
                ('autorizado', models.BooleanField(default=False, verbose_name='Autorización')),
                ('cicloCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.ciclocaja', verbose_name='cicloCaja')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.persona', verbose_name='Persona')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.proveedor', verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Cobros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(verbose_name='precio')),
                ('registroEstacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.registroestacionamiento', verbose_name='registroEstacionamiento')),
            ],
        ),
        migrations.CreateModel(
            name='CicloMensual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cicloMensual', models.IntegerField(verbose_name='cicloMensual')),
                ('cicloAnual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.cicloanual', verbose_name='cicloAnual')),
            ],
        ),
        migrations.AddField(
            model_name='ciclocaja',
            name='cicloMensual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.ciclomensual', verbose_name='cicloMensual'),
        ),
    ]

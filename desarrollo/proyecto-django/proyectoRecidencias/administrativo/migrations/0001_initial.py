# Generated by Django 3.2.4 on 2021-06-26 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600)),
                ('direccion', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=40, unique=True)),
                ('tipo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=100)),
                ('numCuartos', models.IntegerField(verbose_name='numero de cuartos')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='administrativo.edificio')),
            ],
        ),
    ]

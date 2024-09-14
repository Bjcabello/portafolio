# Generated by Django 5.1.1 on 2024-09-13 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades'},
        ),
        migrations.AddField(
            model_name='skill',
            name='icon_url',
            field=models.URLField(blank=True, null=True, verbose_name='Icono de la Habilidad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.CharField(max_length=100, verbose_name='Profesion'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('BASICO', 'Básico'), ('INTERMEDIO', 'Intermedio'), ('AVANZADO', 'Avanzado')], max_length=10, verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='apiapp.profile', verbose_name='Perfil'),
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_alter_skill_options_skill_icon_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon_url',
            field=models.URLField(blank=True, null=True, verbose_name='Icono de Red Social'),
        ),
    ]
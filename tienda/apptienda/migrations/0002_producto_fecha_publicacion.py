# Generated by Django 3.2.4 on 2021-06-22 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

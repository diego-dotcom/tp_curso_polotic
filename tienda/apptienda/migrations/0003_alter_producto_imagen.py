# Generated by Django 3.2.4 on 2021-06-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0002_producto_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(blank=True, upload_to='img_productos/'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-22 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('imagen', models.FileField(blank=True, upload_to='img_products')),
                ('descripcion', models.TextField(default='')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='apptienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('productos', models.ManyToManyField(to='apptienda.Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
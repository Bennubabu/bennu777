# Generated by Django 5.0.1 on 2024-04-25 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='appleImages')),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Anchors', models.URLField(default='http://127.0.0.1:8000/APP/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Oneplus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='oneplusImages')),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Anchors', models.URLField(default='http://127.0.0.1:8000/APP/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=254)),
                ('PhNo', models.IntegerField()),
                ('Address', models.TextField()),
                ('PinCode', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Realme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='realmeImages')),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Anchors', models.URLField(default='http://127.0.0.1:8000/APP/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Redmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='redmiImages')),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Anchors', models.URLField(default='http://127.0.0.1:8000/APP/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='samsungImages')),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Anchors', models.URLField(default='http://127.0.0.1:8000/APP/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('appleproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.apple')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OneplusCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('oneplusproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.oneplus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RealmeCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('realmeproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.realme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RedmiCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('redmiproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.redmi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SamsungCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('samsungproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.samsung')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trend1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.apple')),
                ('Trend2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.oneplus')),
                ('Trend3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.redmi')),
                ('Trend4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.samsung')),
            ],
        ),
    ]

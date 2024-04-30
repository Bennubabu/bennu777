# Generated by Django 5.0.1 on 2024-04-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.IntegerField()),
                ('Verified', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='PaymentMode',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
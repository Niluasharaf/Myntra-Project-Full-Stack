# Generated by Django 4.1.1 on 2023-01-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app8', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=10)),
                ('order_address', models.CharField(max_length=10)),
                ('order_phone', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=10)),
                ('product_price', models.CharField(max_length=10)),
                ('status_1', models.CharField(max_length=10)),
            ],
        ),
    ]

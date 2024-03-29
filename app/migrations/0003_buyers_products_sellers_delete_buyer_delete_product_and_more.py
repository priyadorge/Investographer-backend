# Generated by Django 5.0.1 on 2024-03-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_buyer_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Description', models.CharField(max_length=1000)),
                ('Live', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]

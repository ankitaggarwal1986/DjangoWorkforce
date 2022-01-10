# Generated by Django 3.2.8 on 2022-01-10 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('ContactNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('P_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalePrice', models.IntegerField()),
                ('CustomerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
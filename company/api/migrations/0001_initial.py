# Generated by Django 3.2.8 on 2022-01-10 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActivityHours', models.PositiveIntegerField()),
                ('IdleTime', models.PositiveIntegerField()),
                ('OfficeHours', models.PositiveIntegerField()),
                ('EmpId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2022-01-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='OfficeHours',
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('Name', 'Department')},
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_ems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ems',
            name='ems_name',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_mobileproduct_mobile_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ems_number', models.CharField(max_length=100)),
                ('ems_name', models.TextField(null=True)),
                ('ems_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0004_auto_20200426_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileproduct',
            name='mobile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]

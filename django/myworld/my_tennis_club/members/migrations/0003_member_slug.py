# Generated by Django 4.2.19 on 2025-02-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-24 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_custo_user_userprofile_purchased_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='custo_user',
        ),
    ]

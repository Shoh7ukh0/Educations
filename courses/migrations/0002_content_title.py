# Generated by Django 5.0.2 on 2024-04-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

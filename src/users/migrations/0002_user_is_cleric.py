# Generated by Django 2.2.13 on 2020-08-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cleric',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

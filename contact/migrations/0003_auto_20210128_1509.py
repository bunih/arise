# Generated by Django 3.1.5 on 2021-01-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

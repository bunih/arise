# Generated by Django 3.1.3 on 2021-09-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0002_auto_20210910_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

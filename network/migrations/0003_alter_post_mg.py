# Generated by Django 4.2.3 on 2023-08-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mg',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0041_alter_partido_gc_alter_partido_gf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='suplente',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='titular',
            field=models.IntegerField(default=0),
        ),
    ]

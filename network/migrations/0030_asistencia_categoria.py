# Generated by Django 4.2.3 on 2023-09-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0029_remove_asistencia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='categoria',
            field=models.CharField(default='Default Category', max_length=50),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-04 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_alter_asistencia_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='categoria',
        ),
    ]

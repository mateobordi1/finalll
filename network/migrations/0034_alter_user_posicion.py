# Generated by Django 4.2.3 on 2023-09-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0033_categoria_usuarios_en_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='posicion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

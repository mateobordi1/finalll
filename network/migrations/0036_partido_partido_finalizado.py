# Generated by Django 4.2.3 on 2023-09-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0035_user_convocado_estado_partido'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='partido_finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
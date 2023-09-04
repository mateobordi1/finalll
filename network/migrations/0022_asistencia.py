# Generated by Django 4.2.3 on 2023-09-03 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_remove_categoria_cebollitas_remove_categoria_cuarta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo_asistencia', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20)),
                ('comentarios', models.TextField(blank=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias_jugador', to=settings.AUTH_USER_MODEL)),
                ('tomada_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias_tomadas_por', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

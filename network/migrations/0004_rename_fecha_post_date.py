# Generated by Django 4.2.3 on 2023-08-14 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_post_mg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fecha',
            new_name='date',
        ),
    ]

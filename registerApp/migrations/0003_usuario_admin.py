# Generated by Django 4.1.13 on 2024-01-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerApp', '0002_usuario_id_alter_usuario_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.1 on 2019-12-28 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0027_notificacion_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacionestado',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
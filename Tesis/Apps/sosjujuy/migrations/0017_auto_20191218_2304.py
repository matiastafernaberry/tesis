# Generated by Django 2.1 on 2019-12-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0016_notificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

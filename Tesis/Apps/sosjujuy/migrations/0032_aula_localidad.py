# Generated by Django 2.1 on 2020-01-04 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0031_auto_20200103_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='localidad',
            field=models.CharField(default='', max_length=160),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1 on 2019-12-15 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0012_auto_20191215_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiario',
            name='numero_beneficiario',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-06 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='empresa',
            new_name='empresas',
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_empresa_usuario_empresas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='empresas',
            field=models.ManyToManyField(related_name='usuarios', to='api.Empresa'),
        ),
    ]

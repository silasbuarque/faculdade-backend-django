# Generated by Django 5.1.3 on 2024-11-24 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0001_initial'),
        ('usuarios', '0003_remove_usuario_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacao',
            name='origem',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='usuarios.usuario'),
        ),
    ]
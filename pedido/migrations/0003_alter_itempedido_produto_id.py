# Generated by Django 5.1.7 on 2025-03-14 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_itempedido_produto_id_alter_itempedido_produto'),
        ('produto', '0005_alter_variacao_options_alter_variacao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='produto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto'),
        ),
    ]

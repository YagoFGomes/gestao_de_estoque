# Generated by Django 4.1.3 on 2022-12-03 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_clientes', '0002_remove_cliente_conta_conta_cliente_conta_quantidade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conta',
            old_name='itens',
            new_name='item',
        ),
    ]

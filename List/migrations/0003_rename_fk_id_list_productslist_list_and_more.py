# Generated by Django 4.1.7 on 2023-03-27 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_productslist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productslist',
            old_name='fk_id_list',
            new_name='list',
        ),
        migrations.RenameField(
            model_name='productslist',
            old_name='fk_id_product',
            new_name='product',
        ),
    ]

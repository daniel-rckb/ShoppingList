# Generated by Django 4.2.2 on 2023-06-07 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0002_rename_shoopingitem_shopingitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopingItem',
            new_name='ShoppingItem',
        ),
    ]
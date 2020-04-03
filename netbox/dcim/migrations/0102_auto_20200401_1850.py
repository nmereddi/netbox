# Generated by Django 2.2.11 on 2020-04-01 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0101_auto_20200331_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inventoryitems', to='dcim.InventoryItemRole'),
        ),
    ]

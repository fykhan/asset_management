# Generated by Django 5.0.3 on 2024-04-02 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0003_alter_assetutilization_user_alter_asset_assigned_to_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssetUtilization',
        ),
    ]

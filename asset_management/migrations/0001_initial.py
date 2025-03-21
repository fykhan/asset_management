# Generated by Django 4.2.7 on 2024-03-26 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('barcode', models.CharField(max_length=50, unique=True)),
                ('assigned', models.BooleanField(default=False)),
                ('checkout_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssetUtilization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_management.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_management.user')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset_management.user'),
        ),
    ]

# Generated by Django 3.0 on 2020-03-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_no', models.CharField(max_length=100)),
                ('current_units_balance', models.CharField(max_length=100)),
                ('cumulative_usage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_no', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('token_amount', models.CharField(max_length=100)),
                ('vat', models.CharField(max_length=100)),
                ('fuel_energy_charge', models.CharField(max_length=100)),
                ('forex_charge', models.CharField(max_length=100)),
                ('Epra_charge', models.CharField(max_length=100)),
                ('warma_charge', models.CharField(max_length=100)),
                ('rep_charge', models.CharField(max_length=100)),
                ('inflation_adjustment', models.CharField(max_length=100)),
            ],
        ),
    ]

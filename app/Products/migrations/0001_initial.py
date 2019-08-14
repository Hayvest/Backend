# Generated by Django 2.2.4 on 2019-08-14 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Units', '__first__'),
        ('Categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alternative_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='Categories.Category')),
                ('units_of_measure', models.ManyToManyField(related_name='products', to='Units.Unit')),
            ],
        ),
    ]

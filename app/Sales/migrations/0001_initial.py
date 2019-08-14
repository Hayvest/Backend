# Generated by Django 2.2.4 on 2019-08-14 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('Units', '__first__'),
        ('County', '0001_initial'),
        ('Farm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selling', to='County.County')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='Farm.Farm')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='Products.Product')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Units.Unit')),
            ],
        ),
    ]

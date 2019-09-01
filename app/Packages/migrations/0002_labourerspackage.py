# Generated by Django 2.2.4 on 2019-09-01 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabourersPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number_of_services', models.IntegerField()),
                ('price', models.IntegerField()),
                ('period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='LPackage', to='Packages.Period')),
            ],
        ),
    ]
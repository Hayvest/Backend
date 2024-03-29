# Generated by Django 2.2.4 on 2019-08-14 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Packages', '__first__'),
        ('County', '0001_initial'),
        ('Members', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
                ('package_update_date', models.DateTimeField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='County.County')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='Members.Member')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Packages.FarmPackage')),
            ],
        ),
    ]

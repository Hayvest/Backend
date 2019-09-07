# Generated by Django 2.2.4 on 2019-09-02 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('County', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='County.County')),
            ],
        ),
    ]
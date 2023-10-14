# Generated by Django 4.0.4 on 2022-06-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_childdiseasedetials_2019_20'),
    ]

    operations = [
        migrations.CreateModel(
            name='childvaccinationdetials_2018_19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=20)),
                ('opv0', models.IntegerField()),
                ('bcg', models.IntegerField()),
                ('hep_B0', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='childvaccinationdetials_2019_20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=20)),
                ('opv0', models.IntegerField()),
                ('bcg', models.IntegerField()),
                ('hep_B0', models.IntegerField()),
            ],
        ),
    ]

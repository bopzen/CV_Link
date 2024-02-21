# Generated by Django 5.0.2 on 2024-02-21 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_talent', '0003_talentprofile_introduction_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_talent.talentprofile')),
            ],
        ),
    ]
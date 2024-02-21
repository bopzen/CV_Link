# Generated by Django 5.0.2 on 2024-02-21 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_recruiter', '0003_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('linkedin_profile', models.URLField()),
                ('facebook_profile', models.URLField()),
                ('instagram_profile', models.URLField()),
                ('twitter_profile', models.URLField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_recruiter.recruiterprofile')),
            ],
        ),
    ]

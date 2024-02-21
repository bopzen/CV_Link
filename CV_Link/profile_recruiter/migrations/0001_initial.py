# Generated by Django 5.0.2 on 2024-02-13 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_alter_accountuser_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.TextField(max_length=300)),
                ('company_website', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
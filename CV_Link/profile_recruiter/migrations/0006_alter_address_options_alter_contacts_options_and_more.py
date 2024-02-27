# Generated by Django 5.0.2 on 2024-02-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_recruiter', '0005_alter_address_recruiter_alter_contacts_recruiter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='facebook_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='instagram_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='twitter_profile',
            field=models.URLField(blank=True, null=True),
        ),
    ]
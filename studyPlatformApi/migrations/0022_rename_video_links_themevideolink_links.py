# Generated by Django 4.2.6 on 2023-10-12 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0021_remove_themevideolink_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='themevideolink',
            old_name='video_links',
            new_name='links',
        ),
    ]

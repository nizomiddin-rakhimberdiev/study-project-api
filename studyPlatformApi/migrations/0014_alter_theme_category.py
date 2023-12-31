# Generated by Django 4.2.6 on 2023-10-11 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0013_category_has_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='category',
            field=models.ForeignKey(limit_choices_to={'parent_category__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='studyPlatformApi.category'),
        ),
    ]

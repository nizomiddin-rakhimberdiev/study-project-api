# Generated by Django 4.2.6 on 2023-10-30 18:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('studyPlatformApi', '0028_themeimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/', verbose_name='Category Image'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Subject Name')),
                ('subjects', models.ManyToManyField(related_name='subjects', to='studyPlatformApi.subject')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='courses',
            field=models.ManyToManyField(related_name='categories', to='studyPlatformApi.course'),
        ),
    ]

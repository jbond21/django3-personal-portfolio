# Generated by Django 3.0.7 on 2020-07-17 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='portfolio/images/'),
            preserve_default=False,
        ),
    ]

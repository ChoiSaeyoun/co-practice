# Generated by Django 3.2.5 on 2021-09-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_image_detection_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
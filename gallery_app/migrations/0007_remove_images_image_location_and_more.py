# Generated by Django 4.0.4 on 2022-05-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0006_rename_names_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_location',
        ),
        migrations.RemoveField(
            model_name='images',
            name='image_category',
        ),
        migrations.AddField(
            model_name='images',
            name='image_category',
            field=models.ManyToManyField(to='gallery_app.category'),
        ),
    ]
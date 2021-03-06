# Generated by Django 4.0.4 on 2022-05-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_images_gallery_image_alter_images_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='category',
            field=models.ManyToManyField(to='gallery_app.category'),
        ),
    ]

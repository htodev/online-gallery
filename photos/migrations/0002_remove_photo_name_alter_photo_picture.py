# Generated by Django 4.0.6 on 2022-09-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
    ]

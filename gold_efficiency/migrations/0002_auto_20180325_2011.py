# Generated by Django 2.0.3 on 2018-03-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gold_efficiency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image_json',
            new_name='img',
        ),
    ]

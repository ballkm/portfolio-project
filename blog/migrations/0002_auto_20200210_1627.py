# Generated by Django 2.2.10 on 2020-02-10 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='iamge',
            new_name='image',
        ),
    ]

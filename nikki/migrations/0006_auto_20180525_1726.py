# Generated by Django 2.0.5 on 2018-05-25 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nikki', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='test',
            new_name='text',
        ),
    ]

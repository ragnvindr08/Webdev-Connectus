# Generated by Django 4.2.11 on 2024-05-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]

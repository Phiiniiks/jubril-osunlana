# Generated by Django 3.2.5 on 2021-10-20 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='Subject',
        ),
    ]

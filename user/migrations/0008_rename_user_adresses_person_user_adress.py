# Generated by Django 3.2.16 on 2022-12-21 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_user_adresses_person_user_adresses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_adresses',
            new_name='user_adress',
        ),
    ]

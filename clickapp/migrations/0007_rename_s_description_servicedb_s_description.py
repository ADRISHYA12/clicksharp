# Generated by Django 4.2.3 on 2023-08-03 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clickapp', '0006_servicedb_alter_saveitemdb_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedb',
            old_name='S_description',
            new_name='S_DESCRIPTION',
        ),
    ]

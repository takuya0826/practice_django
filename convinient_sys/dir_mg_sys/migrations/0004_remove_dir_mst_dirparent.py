# Generated by Django 4.1.4 on 2022-12-30 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dir_mg_sys', '0003_alter_dir_mst_dirparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dir_mst',
            name='dirparent',
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-04 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dir_mg_sys', '0002_rename_dirmanager_id_dir_mst_dirmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dir_mst',
            name='dirmanager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dir_mg_sys.user_mst'),
        ),
    ]
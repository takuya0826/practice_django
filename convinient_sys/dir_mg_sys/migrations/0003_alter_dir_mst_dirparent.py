# Generated by Django 4.1.4 on 2022-12-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir_mg_sys', '0002_dir_mst_dirparent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dir_mst',
            name='dirparent',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
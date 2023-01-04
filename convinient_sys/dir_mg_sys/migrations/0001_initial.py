# Generated by Django 4.1.4 on 2023-01-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group_mst',
            fields=[
                ('group_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_mst',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='group_organaization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, null=True)),
                ('user_name', models.CharField(max_length=100)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dir_mg_sys.group_mst')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dir_mg_sys.user_mst')),
            ],
        ),
        migrations.CreateModel(
            name='dir_mst',
            fields=[
                ('dirpath', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('dirvolume', models.IntegerField()),
                ('dirmanager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dir_mg_sys.user_mst')),
                ('dirphase', models.IntegerField()),
            ],
            options={
                'ordering': ['dirpath'],
            },
        ),
        migrations.CreateModel(
            name='access_mst_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('authority', models.CharField(choices=[('F', 'フルコントロール'), ('W', '更新権'), ('R', '検索権')], max_length=50)),
                ('dirpath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dir_mg_sys.dir_mst')),
            ],
        ),
        migrations.CreateModel(
            name='access_mst_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('authority', models.CharField(choices=[('F', 'フルコントロール'), ('W', '更新権'), ('R', '検索権')], max_length=50)),
                ('dirpath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dir_mg_sys.dir_mst')),
            ],
        ),
    ]

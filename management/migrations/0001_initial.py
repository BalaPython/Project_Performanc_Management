# Generated by Django 2.0.5 on 2021-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manreg',
            fields=[
                ('man_id', models.AutoField(primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=300)),
                ('pword', models.CharField(max_length=20)),
                ('conpword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='projmodule',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('module_proj', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=50)),
                ('deadline_date', models.CharField(max_length=50)),
                ('ass_to', models.CharField(max_length=300)),
                ('ass_date', models.CharField(max_length=50)),
                ('paper', models.FileField(upload_to='')),
                ('proj_status', models.CharField(max_length=100)),
                ('proj_percentage', models.CharField(max_length=20)),
                ('ass_man_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='team_add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addteam', models.CharField(max_length=30)),
            ],
        ),
    ]

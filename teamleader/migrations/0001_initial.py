# Generated by Django 2.0.5 on 2021-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tl_assignto_team',
            fields=[
                ('tl_ass_id', models.AutoField(primary_key=True, serialize=False)),
                ('tl_module_proj', models.CharField(max_length=100)),
                ('tl_start_date', models.CharField(max_length=50)),
                ('tl_deadline_date', models.CharField(max_length=50)),
                ('tl_ass_to', models.CharField(max_length=300)),
                ('tl_ass_date', models.CharField(max_length=50)),
                ('tl_paper', models.CharField(max_length=500)),
                ('tl_proj_status', models.CharField(max_length=300)),
                ('tl_proj_percentage', models.CharField(max_length=300)),
                ('man_module_id', models.CharField(max_length=50)),
                ('tl_ass_man_id', models.CharField(max_length=50)),
                ('proj_reason', models.CharField(max_length=300)),
                ('status_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tl_regis',
            fields=[
                ('tl_id', models.AutoField(primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=300)),
                ('pword', models.CharField(max_length=20)),
                ('conpword', models.CharField(max_length=20)),
                ('spec_module', models.CharField(max_length=50)),
                ('tl_team_name', models.CharField(max_length=20)),
            ],
        ),
    ]
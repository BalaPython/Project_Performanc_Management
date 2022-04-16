# Generated by Django 2.0.5 on 2021-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daily_status_upd',
            fields=[
                ('daily_id', models.AutoField(primary_key=True, serialize=False)),
                ('man_module_id', models.CharField(max_length=300)),
                ('emp_man_id', models.CharField(max_length=300)),
                ('emp_mail', models.CharField(max_length=300)),
                ('emp_reg_id', models.CharField(max_length=50)),
                ('emp_team', models.CharField(max_length=50)),
                ('empfn', models.CharField(max_length=100)),
                ('empln', models.CharField(max_length=100)),
                ('emp_module_proj', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('work_completion', models.IntegerField()),
                ('reason', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='emp_workstatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_module_proj', models.CharField(max_length=100)),
                ('emp_start_date', models.CharField(max_length=50)),
                ('emp_deadline_date', models.CharField(max_length=50)),
                ('emp_ass_to', models.CharField(max_length=300)),
                ('emp_ass_date', models.CharField(max_length=50)),
                ('emp_paper', models.CharField(max_length=500)),
                ('emp_ass_member', models.CharField(max_length=300)),
                ('emp_percentage', models.CharField(max_length=300)),
                ('emp_reason', models.CharField(max_length=500)),
                ('emp_tl_ass_id', models.CharField(max_length=300)),
                ('man_module_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='regis',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=300)),
                ('pword', models.CharField(max_length=20)),
                ('conpword', models.CharField(max_length=20)),
                ('emp_module', models.CharField(max_length=50)),
                ('emp_team_name', models.CharField(max_length=20)),
            ],
        ),
    ]
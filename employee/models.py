from django.db import models

# Create your models here.
from teamleader.models import tl_assignto_team


class regis(models.Model):
    emp_id =  models.AutoField(primary_key=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    mail = models.CharField(max_length=300)
    pword = models.CharField(max_length=20)
    conpword = models.CharField(max_length=20)
    emp_module = models.CharField(max_length=50)
    emp_team_name = models.CharField(max_length=20)
    def __str__(self):
        return self.emp_id

class emp_workstatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    emp_module_proj = models.CharField(max_length=100)
    emp_start_date = models.CharField(max_length=50)
    emp_deadline_date = models.CharField(max_length=50)
    emp_ass_to = models.CharField(max_length=300)
    emp_ass_date = models.CharField(max_length=50)
    emp_paper = models.CharField(max_length=500)
    emp_ass_member = models.CharField(max_length=300)
    emp_percentage = models.CharField(max_length=300)
    emp_reason = models.CharField(max_length=500)
    emp_tl_ass_id = models.CharField(max_length=300)
    man_module_id = models.CharField(max_length=300)
    def __str__(self):
        return self.man_module_id

class daily_status_upd(models.Model):
    daily_id = models.AutoField(primary_key=True)
    man_module_id = models.CharField(max_length=300)
    emp_man_id = models.CharField(max_length=300)
    emp_mail = models.CharField(max_length=300)
    emp_reg_id = models.CharField(max_length=50)
    emp_team = models.CharField(max_length=50)
    empfn = models.CharField(max_length=100)
    empln = models.CharField(max_length=100)
    emp_module_proj = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    work_completion = models.IntegerField()
    reason = models.CharField(max_length=300)
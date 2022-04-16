from django.db import models

# Create your models here.

class tl_regis(models.Model):
    tl_id =  models.AutoField(primary_key=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    mail = models.CharField(max_length=300)
    pword = models.CharField(max_length=20)
    conpword = models.CharField(max_length=20)
    spec_module = models.CharField(max_length=50)
    tl_team_name = models.CharField(max_length=20)
    def __str__(self):
        return self.tl_id

class tl_assignto_team(models.Model):
    tl_ass_id = models.AutoField(primary_key=True)
    tl_module_proj = models.CharField(max_length=100)
    tl_start_date = models.CharField(max_length=50)
    tl_deadline_date = models.CharField(max_length=50)
    tl_ass_to = models.CharField(max_length=300)
    tl_ass_date = models.CharField(max_length=50)
    tl_paper = models.CharField(max_length=500)
    tl_proj_status = models.CharField(max_length=300)
    tl_proj_percentage = models.CharField(max_length=300)
    man_module_id = models.CharField(max_length=50)
    tl_ass_man_id = models.CharField(max_length=50)
    proj_reason = models.CharField(max_length=300)
    status_date = models.CharField(max_length=50)
    def __str__(self):
        return self.man_module_id
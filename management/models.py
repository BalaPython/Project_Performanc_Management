from django.db import models

# Create your models here.

class manreg(models.Model):
    man_id =  models.AutoField(primary_key=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    mail = models.CharField(max_length=300)
    pword = models.CharField(max_length=20)
    conpword = models.CharField(max_length=20)
    def __str__(self):
        return self.man_id

class projmodule(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_proj = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    deadline_date = models.CharField(max_length=50)
    ass_to = models.CharField(max_length=300)
    ass_date = models.CharField(max_length=50)
    paper = models.FileField()
    proj_status = models.CharField(max_length=100)
    proj_percentage = models.CharField(max_length=20)
    ass_man_id = models.CharField(max_length=50)
    def __str__(self):
        return self.module_id

class team_add(models.Model):
    addteam = models.CharField(max_length=30)
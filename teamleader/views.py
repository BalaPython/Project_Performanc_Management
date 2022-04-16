import docx
from django.shortcuts import render, redirect
from Project_Performance_Management import settings

# Create your views here.
from employee.models import regis, emp_workstatus, daily_status_upd

from management.models import projmodule, team_add
from teamleader.models import tl_regis, tl_assignto_team
from os.path import dirname
import os.path
def tl_home(request):
    display_mail = tl_regis.objects.get(tl_team_name=request.session['teamid'])
    dismail = display_mail.mail
    return render(request,'teamleader_user/tl_home.html', {'name':dismail})

def tl_login(request):
    if request.method == "POST":
        username = request.POST.get('tl')
        password = request.POST.get('passwd')
        a = tl_regis.objects.get(mail=username, pword=password)
        if a:
            request.session['teamid'] = a.tl_team_name
            return redirect('tl_home')
        else:
            return redirect('tl_login')
    return render(request,'teamleader_user/tl_login.html')

def tl_reg(request):
    context = {
        "module_count": ['Design', 'Developer_Frontend', 'Developer_Backend', 'Coding', 'Testing', 'Business_Analyst'],
    }
    teamdata = team_add.objects.all()
    tl = ""
    teaml = ""
    if request.method == "POST":
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        mail = request.POST.get('mail')
        pword = request.POST.get('pword')
        conpword = request.POST.get('conpword')
        specific_mod = request.POST.get('spec_mod')
        team = request.POST.get('team')
        if tl_regis.objects.filter(tl_team_name=team):
            teaml = "Already Team Leader exists, choose other Team"
        else:
            tl_regis.objects.create(fn=firstname, ln=lastname, mail=mail, pword=pword, conpword=conpword, spec_module=specific_mod, tl_team_name=team)
            tl = "Sign up completed successfully "
    return render(request,'teamleader_user/tl_reg.html', {'tl_teamnumber':context, 'teamdet':teamdata, 'tl':tl, 'teaml':teaml})

def tl_workallocation(request):
#   bb=""
    doc = ""
    man_allocate = projmodule.objects.filter(ass_to=request.session['teamid'])
    for i in man_allocate:
        doc = i.paper.url
#   Open and display file in web broswer(view page).
#   d=doc[6:]
#   eod=settings.MEDIA_ROOT+d
#   f=open(eod,'r')
#   doc1=docx.Document(eod)
#   for i in doc1.paragraphs:
#       bb=bb+i.text
#   f.close()
    return render(request,'teamleader_user/tl_workallocation.html', {'view_worklist':man_allocate, 'team_id':request.session["teamid"], 'fopen':doc})

def tl_allocate_work(request,pk):
    assign_tl_msg=""
    assign_sucess_msg=""
    ass = projmodule.objects.get(module_id=pk)
    path = ass.paper.url
    unique_id = ass.module_id
    print(unique_id)
    tl_manid = ass.ass_man_id
    if request.method == "POST":
        tl_module_proj = ass.module_proj
        tl_start_date = ass.start_date
        tl_deadline_date = ass.deadline_date
        tl_ass_to = ass.ass_to
        tl_ass_date = ass.ass_date
        tl_paper = path
        tl_man_module_id = unique_id
        tlass_man_id = tl_manid
        tl_projstatus = "Pending"
        tl_projpercentage = 0
        status_date1 = "yet to start"
        if tl_assignto_team.objects.filter(man_module_id=tl_man_module_id):
            assign_tl_msg = "Already project assigned to different user"
        else:
            tl_assignto_team.objects.create(tl_module_proj=tl_module_proj, tl_start_date=tl_start_date, tl_deadline_date=tl_deadline_date,
                            tl_ass_to=tl_ass_to, tl_ass_date=tl_ass_date, tl_paper=tl_paper,man_module_id=tl_man_module_id,
                            tl_ass_man_id=tlass_man_id,tl_proj_status=tl_projstatus, tl_proj_percentage=tl_projpercentage,
                            status_date=status_date1)
            assign_sucess_msg = "Project successfully assigned to user"
    return render(request,'teamleader_user/tl_allocate_work.html', {'ta':ass, 'fopen':path, 'atmsg':assign_tl_msg, 'asmsg':assign_sucess_msg})

def tl_viewreport(request):
    report = tl_assignto_team.objects.filter(tl_ass_to=request.session['teamid'])
    return render(request,'teamleader_user/tl_viewreport.html',{'team_report':report, 'session':request.session['teamid']})

def proj_status_report(request,pk):
    view_status = daily_status_upd.objects.filter(man_module_id=pk, emp_team=request.session['teamid'])
    details = tl_assignto_team.objects.filter(tl_ass_to=request.session['teamid'], man_module_id=pk)
    if request.method == 'POST':
        status_proj_tl =request.POST.get('status_proj')
        #print(status_proj_tl)
        projmodule.objects.filter(module_id=pk).update(proj_status=status_proj_tl)
        tl_assignto_team.objects.filter(man_module_id=pk).update(tl_proj_status=status_proj_tl)
        return redirect('tl_viewreport')
    return render(request, 'teamleader_user/proj_status_report.html',{'report1':details,'report2':view_status, 'session':request.session['teamid']})

def tl_teamwise_report(request):
    session1 = request.session['teamid']
    view_status = daily_status_upd.objects.filter(emp_team=session1)
    for i in view_status:
        project_user = i.man_module_id
        proj_mod = i.emp_module_proj
    details = tl_assignto_team.objects.filter(tl_ass_to=request.session['teamid'], man_module_id=project_user, tl_module_proj=proj_mod)
    return render(request, 'teamleader_user/tl_teamwise_report.html',{'report1':details,'report2':view_status, 'session':session1})

def tl_status_update_manager(request):
    st_mail = []
    st_per = []
    empstatus = emp_workstatus.objects.filter(emp_ass_to=request.session['teamid'])
    #for i in empstatus:
    #    print(i.emp_percentage)
    #    print(i.man_module_id)
    tsr = tl_assignto_team.objects.filter(tl_ass_to=request.session['teamid'])
    #for i in tsr:
    #    print(i.man_module_id)
        #a = emp_workstatus.objects.filter(emp_tl_ass_id=b)
        #print(a.emp_percentage)
        #if a:
         #   sts_mail = i.tl_ass_member
         #   sts_per = a.emp_percentage
         #   st_mail.append(sts_mail)
         #   st_per.append(sts_per)
        #print(st_mail,st_per)
    #if request.method == "POST":
     #  sts_module_proj = tsr.tl_module_proj
       # sts_start_date = tsr.tl_start_date
      #  sts_deadline_date = tsr.tl_deadline_date
       # sts_ass_to = tsr.tl_ass_to
        #sts_ass_date = tsr.tl_ass_date
     #   sts_paper = tsr.tl_paper
      #  sts_ass_member = tsr.tl_ass_member
    return render(request, 'teamleader_user/tl_status_update_manager.html',{'team_status_report':tsr})

def tl_logout(request):
    del request.session['teamid']
    return render(request,'teamleader_user/tl_logout.html')
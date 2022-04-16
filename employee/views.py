from django.db import connection
from datetime import datetime
from django.shortcuts import render, redirect


# Create your views here.
from employee.models import regis, emp_workstatus, daily_status_upd
from management.models import team_add, projmodule
from teamleader.models import tl_assignto_team


def home(request):
    return render(request, 'employee_user/home.html')

def emp_login(request):
    if request.method == "POST":
            username = request.POST.get('emp')
            password = request.POST.get('password')
            a = regis.objects.get(mail=username, pword=password)
            if a:
                request.session['userid'] = a.mail
                return redirect('emp_home')
            else:
                return redirect('emp_login')
    return render(request, 'employee_user/emp_login.html')

def emp_reg(request):
    msg=""
    msg1=""
    context = {
        "module_count": ['Design', 'Developer_Frontend', 'Developer_Backend', 'Coding', 'Testing', 'Business_Analyst'],
    }
    td = team_add.objects.all()
    if request.method == "POST":
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        mail = request.POST.get('mail')
        pword = request.POST.get('pword')
        conpword = request.POST.get('conpword')
        empmodule = request.POST.get('emp_mod')
        team = request.POST.get('team')
        if regis.objects.filter(mail=mail):
            msg = "Mail Id Already created, try with new mail id"
        else:
            regis.objects.create(fn=firstname, ln=lastname, mail=mail, pword=pword, conpword=conpword, emp_module=empmodule, emp_team_name=team)
            msg1 = "You have been successfully registrated"
    return render(request, 'employee_user/emp_reg.html', {'emp_teamnumber':context,'teamdata':td, 'msg':msg, 'msg1':msg1})

def emp_home(request):
    return render(request, 'employee_user/emp_home.html', {'empwork_id':request.session["userid"]})

def emp_viewallocation(request):
    emp_view = regis.objects.filter(mail=request.session['userid'])
    for i in emp_view:
        team_check= i.emp_team_name
    #print(team_check)
    emp_allocation = tl_assignto_team.objects.filter(tl_ass_to=team_check)
    #for i in emp_allocation:
     #   print(i.man_module_id,"project id")
    #tl_mod = emp_allocation.tl_module_proj
    #mod_emp = regis.objects.filter(emp_module=tl_mod)
    #work_allocat = tl_assignto_team.objects.filter(tl_ass_member=request.session['userid'], )
    return render(request, 'employee_user/emp_viewallocation.html', {'view_work':emp_allocation, 'empwork_id':request.session["userid"]})

def emp_work_status(request,pk):
    emp_alert = ""
    emp_sta = ""
    sts = tl_assignto_team.objects.get(tl_ass_id=pk)
    con = {
        "percentage": ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100'],
    }
    a=sts.tl_ass_id
    #print(a)
    if request.method == "POST":
        emp_module_proj = sts.tl_module_proj
        emp_start_date = sts.tl_start_date
        emp_deadline_date = sts.tl_deadline_date
        emp_ass_to = sts.tl_ass_to
        emp_ass_date = sts.tl_ass_date
        emp_paper = sts.tl_paper
        emp_ass_member = sts.tl_ass_member
        #emp_percentage =
        #emp_reason =
        emp_ass_id = sts.tl_ass_id
        emp_man_module_id = sts.man_module_id
        if emp_workstatus.objects.filter(emp_tl_ass_id=emp_ass_id,):
            emp_alert = "Status Already updated,Completed the assigned work"
        else:
            emp_workstatus.objects.create(emp_module_proj = emp_module_proj, emp_start_date = emp_start_date,
                                      emp_deadline_date = emp_deadline_date, emp_ass_to = emp_ass_to,
                                      emp_ass_date = emp_ass_date, emp_paper = emp_paper, emp_ass_member = emp_ass_member,
                                      emp_percentage = emp_percentage, emp_reason = emp_reason, emp_tl_ass_id = emp_ass_id,
                                          man_module_id=emp_man_module_id)
            emp_sta = "Project Status has been updated successfully"
    return render(request, 'employee_user/emp_work_status.html', {'es':sts, 'p':con, 'alert':emp_alert, 'emp_alt':emp_sta})

def viewreport(request):
    emp_data = regis.objects.filter(mail=request.session['userid'])
    for i in emp_data:
        team_user = i.emp_team_name
    view_status = daily_status_upd.objects.filter(emp_mail=request.session['userid'], emp_team=team_user)
    for i in view_status:
        project_user = i.man_module_id
        proj_mod = i.emp_module_proj
    details = tl_assignto_team.objects.filter(tl_ass_to=team_user, man_module_id=project_user, tl_module_proj=proj_mod)
    return render(request, 'employee_user/viewreport.html',{'report1':details,'report2':view_status, 'empwork_id':request.session["userid"]})

def emp_daily_status(request,pk):
    date1=''
    con = {
        "percentage": ['5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100'],
    }
    msg=""
    msg1=""
    msg2=""
    emp_table = regis.objects.get(mail=request.session['userid'])
    emp_allocation = tl_assignto_team.objects.get(man_module_id=pk)
    proj_ass_date_sts = emp_allocation.tl_ass_date
    proj_dead_date_sts = emp_allocation.tl_deadline_date
    #print("Assigned date",proj_ass_date_sts, "Deadline Date",proj_dead_date_sts)
    #working_days = proj_dead_date_sts-proj_ass_date_sts
    #print("Number of Days for completing the project",working_days)
    date1 = datetime.today().strftime('%Y-%m-%d')
    if request.method == "POST":
        man_module_id1 = emp_allocation.man_module_id
        emp_man_id1 = emp_allocation.tl_ass_man_id
        emp_mail1 = emp_table.mail
        emp_reg_id1 = emp_table.emp_id
        emp_team1 = emp_table.emp_team_name
        emp_fn = emp_table.fn
        emp_ln = emp_table.ln
        emp_module_proj1 = emp_allocation.tl_module_proj
        #date1 = request.POST.get('daily_date')
        #print("Choose date",date1, man_module_id1)
        work_completion1 = request.POST.get('daily_per')
        reason = request.POST.get('reason')
        if proj_ass_date_sts > date1:
            msg2 = "Choose date within project timeline"
        elif proj_dead_date_sts < date1:
            msg2 = "Choose date within project timeline"
        elif daily_status_upd.objects.filter(date=date1, emp_mail=emp_mail1):
            msg = "Daily status already updated"
        else:
            daily_status_upd.objects.create(man_module_id=man_module_id1, emp_man_id=emp_man_id1, date=date1,
                                                work_completion=work_completion1, reason=reason, emp_mail= emp_mail1,
                                            emp_reg_id=emp_reg_id1, emp_team=emp_team1, empfn=emp_fn, empln=emp_ln, emp_module_proj=emp_module_proj1)
            if proj_dead_date_sts == date1:
                tl_assignto_team.objects.filter(man_module_id=pk, tl_deadline_date=date1).update(tl_proj_percentage=work_completion1,
                    proj_reason=reason,status_date=date1)
                msg1 = "Status for final day of project has been updated successfully"
            else:
                tl_assignto_team.objects.filter(man_module_id=pk).update(tl_proj_percentage=work_completion1,
                    proj_reason=reason,status_date=date1)
                msg1 = "Current day status updated successfully"
    return render(request, 'employee_user/emp_daily_status.html',{'p':con, 'fail':msg, 'suces':msg1, 'datereg':msg2, 'data':emp_allocation, 'date_today':date1})

def emp_logout(request):
    del request.session['userid']
    return render(request, 'employee_user/emp_logout.html')
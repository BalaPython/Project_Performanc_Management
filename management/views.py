from django.db import connection
from django.db.models import Count, Q
from django.shortcuts import render, redirect

# Create your views here.
from employee.models import daily_status_upd
from management.models import manreg, projmodule, team_add
from teamleader.models import tl_assignto_team

def man_login(request):
    if request.method == "POST":
        username = request.POST.get('man')
        password = request.POST.get('pwd')
        a = manreg.objects.get(mail=username, pword=password)
        if a:
            request.session['manid'] = a.man_id
            return redirect('man_home')
        else:
            return redirect('man_login')
    return render(request, 'management_admin/man_login.html')

def man_reg(request):
    if request.method == "POST":
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        mail = request.POST.get('mail')
        pword = request.POST.get('pword')
        conpword = request.POST.get('conpword')
        manreg.objects.create(fn=firstname, ln=lastname, mail=mail, pword=pword, conpword=conpword)
        return redirect('man_reg')
    return render(request, 'management_admin/man_reg.html')

def man_home(request):
    display_mail = manreg.objects.get(man_id=request.session['manid'])
    dismail = display_mail.mail
    return render(request,'management_admin/man_home.html', {'name':dismail})

def projectplan(request):
    return render(request,'management_admin/projectplan.html')

def man_module(request):
    context = {
        "module_count":['Design', 'Developer_Frontend', 'Developer_Backend', 'Coding', 'Testing', 'Business_Analyst'],
    }
    team_ass = ""
    assign_team = ""
    Assign_teamname = team_add.objects.all()
    ass_man = manreg.objects.get(man_id=request.session['manid'])
    if request.method == "POST" and request.FILES['abstract']:
        workdev = request.POST.get('module')
        startdate =request.POST.get('start_date')
        deadline_date = request.POST.get('deadline_date')
        assign_to = request.POST.get('tl_team_name')
        assign_date = request.POST.get('assigned_date')
        abstract = request.FILES['abstract']
        status = "Pending"
        ass_man_id = ass_man.man_id
        if projmodule.objects.filter(module_proj=workdev, ass_to=assign_to):
            team_ass = "Already team selected, choose other team"
        else:
            assign_team = "Successfully Assigned the Work"
            projmodule.objects.create(module_proj=workdev, start_date=startdate, deadline_date=deadline_date, ass_to=assign_to,
                                      ass_date=assign_date, paper=abstract, proj_status=status, ass_man_id=ass_man_id)
    return render(request,'management_admin/man_module.html', {'project_module':context, 'tltname':Assign_teamname, 'ta':team_ass, 'ass_team':assign_team})

def man_addteam(request):
    new_team=""
    tc=""
    if request.method == "POST":
        add_t = request.POST.get('add_new_team')
        if team_add.objects.filter(addteam=add_t):
            new_team = "Already team created, create new team"
        else:
            team_add.objects.create(addteam=add_t)
            tc="New Team has been created successfully"
    display_mail = manreg.objects.get(man_id=request.session['manid'])
    dismail = display_mail.mail
    return render(request,'management_admin/man_addteam.html', {'newteam':new_team, 'teamcreated':tc, 'name':dismail})

def man_viewreport(request):
    report = tl_assignto_team.objects.filter(tl_ass_man_id=request.session['manid'])
    return render(request,'management_admin/man_viewreport.html', {'proj_report':report})

def overall_status_report(request,pk):
    details = tl_assignto_team.objects.filter(man_module_id=pk)
    view_status = daily_status_upd.objects.filter(man_module_id=pk)
    return render(request, 'management_admin/overall_status_report.html',{'report1':details,'report2':view_status})

def man_consolidate_report(request):
    cursor = connection.cursor()
    query = "select tl.tl_module_proj, tl.tl_ass_to, tl.tl_start_date, tl.tl_deadline_date, tl.tl_ass_date, " \
            "tl.tl_paper, es.emp_mail, es.date, es.work_completion, tl.tl_proj_status, es.reason, " \
            "es.man_module_id, tl.tl_ass_man_id from employee_daily_status_upd as es " \
            "left join teamleader_tl_assignto_team as tl on es.man_module_id = tl.man_module_id " \
            "where tl.tl_ass_man_id = "+ str(request.session['manid']) +" order by es.man_module_id;"
    cursor.execute(query)
    print(query)
    res = cursor.fetchall()
    return render(request, 'management_admin/man_consolidate_report.html', {'result':res})

def man_projwise_delay(request,pk):
    cursor = connection.cursor()
    query = "select es.emp_module_proj, es.emp_team, tl.tl_start_date, tl.tl_deadline_date, tl.tl_ass_date, tl.tl_paper," \
            "es.emp_mail, es.date, es.work_completion, tl.tl_proj_status, es.reason, es.man_module_id, Count(es.work_completion) from employee_daily_status_upd as es left join teamleader_tl_assignto_team as " \
            "tl on es.man_module_id = tl.man_module_id where es.work_completion <="+ str(30) +" and tl.tl_ass_man_id = "+ str(request.session['manid']) +" and es.man_module_id =" + str(pk) +" group by es.emp_mail having(Count(es.work_completion)>=5); "
    cursor.execute(query)
    res = cursor.fetchall()
    result = daily_status_upd.objects.values('emp_mail').filter(man_module_id=pk, emp_man_id=request.session['manid']).filter(work_completion__lte ='30').annotate(dcount=Count('emp_mail'))
    print(result)
    i=0
    val_record1=""
    for cnt in result:
        if cnt['dcount'] >= 5:
            val_record1 = daily_status_upd.objects.filter(man_module_id=pk, emp_man_id=request.session['manid'],
                                                          work_completion__lte=30, emp_mail=cnt['emp_mail']).values()
            if i==0:
                val_record = val_record1
            else :
                val_record1=val_record1|val_record
                print(val_record1)
            i=i+1
    return render(request, 'management_admin/man_projwise_delay.html', {'result':res, 'display':val_record1})

def man_viewchart(request):
    display_mail = manreg.objects.get(man_id=request.session['manid'])
    dismail = display_mail.mail
    chart=""
    #if request.method == "POST":
    date_chart1 = request.POST.get('date_chart')
    print(date_chart1)
    chart = daily_status_upd.objects.filter(date=date_chart1,emp_man_id=request.session['manid']).values('emp_mail','work_completion')
    print(chart)
    return render(request,'management_admin/man_viewchart.html', {'objects':chart, 'name':dismail})

def logout(request):
    del request.session['manid']
    return render(request,'management_admin/logout.html')
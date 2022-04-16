"""Project_Performance_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from employee import views as empviews
from management import views as manviews
from teamleader import views as teamviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', empviews.home, name="home"),
    url('^emp_login/$', empviews.emp_login, name="emp_login"),
    url('^emp_reg/$', empviews.emp_reg, name="emp_reg"),
    url('^emp_home/$', empviews.emp_home, name="emp_home"),
    url('^emp_viewallocation/$', empviews.emp_viewallocation, name="emp_viewallocation"),
    url('^emp_work_status/(?P<pk>\d+)/$', empviews.emp_work_status, name="emp_work_status"),
    url('^emp_daily_status/(?P<pk>\d+)/$', empviews.emp_daily_status, name="emp_daily_status"),
    url('^viewreport/$', empviews.viewreport, name="viewreport"),
    url('^emp_logout/$', empviews.emp_logout, name="emp_logout"),
    url('^tl_login/$', teamviews.tl_login, name="tl_login"),
    url('^tl_reg/$', teamviews.tl_reg, name="tl_reg"),
    url('^tl_home/$', teamviews.tl_home, name="tl_home"),
    url('^tl_workallocation/$', teamviews.tl_workallocation, name="tl_workallocation"),
    url('^tl_allocate_work/(?P<pk>\d+)/$', teamviews.tl_allocate_work, name="tl_allocate_work"),
    url('^proj_status_report/(?P<pk>\d+)/$', teamviews.proj_status_report, name="proj_status_report"),
    url('^tl_viewreport/$', teamviews.tl_viewreport, name="tl_viewreport"),
    url('^tl_teamwise_report/$', teamviews.tl_teamwise_report, name="tl_teamwise_report"),
    url('^tl_logout/$', teamviews.tl_logout, name="tl_logout"),
    url('^man_login/$', manviews.man_login, name="man_login"),
    url('^man_reg/$', manviews.man_reg, name="man_reg"),
    url('^man_home/$', manviews.man_home, name="man_home"),
    url('^man_module/$',manviews.man_module, name="man_module"),
    url('^man_addteam/$',manviews.man_addteam, name="man_addteam"),
    url('^man_viewchart/$',manviews.man_viewchart, name="man_viewchart"),
    url('^projectplan/$',manviews.projectplan, name="projectplan"),
    url('^man_viewreport/$',manviews.man_viewreport, name="man_viewreport"),
    url('^overall_status_report/(?P<pk>\d+)/$',manviews.overall_status_report, name="overall_status_report"),
    url('^man_projwise_delay/(?P<pk>\d+)/$',manviews.man_projwise_delay, name="man_projwise_delay"),
    url('^man_consolidate_report/$',manviews.man_consolidate_report, name="man_consolidate_report"),
    url('^logout/$', manviews.logout, name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
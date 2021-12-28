from django.urls import re_path
from django.urls import path
from django.conf import settings

from jobs import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # Job list
    path("joblist/", views.joblist, name="joblist"),

    # Admin page to create HR account:
    path('create_hr_user/', views.create_hr_user, name='create_hr_user'),

    # Job details
    #url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    path('job/<int:job_id>/', views.detail, name='detail'),

    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    path('sentry-debug/', trigger_error),

    # Homepage automatically redirects to job list
    #url(r"^$", views.joblist, name="name"),
    path("", views.joblist, name="name"),

]

if settings.DEBUG :
    # View page with XSS vulnerability,
    urlpatterns += [re_path(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]
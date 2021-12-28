from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


# Candidate degree types
DEGREE_TYPE = ((u'Bachelor', u'Bachelor'), (u'Master', u'Master'), (u'PhD', u'PhD'))

JobTypes = [
    (0,"Technical"),
    (1,"Product"),
    (2,"Operations"),
    (3,"Design"),
    (4,"Marketing")
]

Cities = [
    (0,"Beijing"),
    (1,"Shanghai"),
    (2,"Shenzhen"),
    (3,"Hangzhou"),
    (4,"Guangzhou")
]


class Job(models.Model):
    # Translators: Job entity translation
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name=_("Job Type"))
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("Job Name"))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_("Job Location"))
    job_responsibility = models.TextField(max_length=1024, verbose_name=_("Job Responsibility"))
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name=_("Job Requirement"))
    creator = models.ForeignKey(User, verbose_name=_("Creator"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("Created Date"), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_("Modified Date"), auto_now=True)

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Job List')

    def __str__(self):
        return self.job_name


class Resume(models.Model):
    # Translators: Resume entity translation
    username = models.CharField(max_length=135, verbose_name=_('Name'))
    applicant = models.ForeignKey(User, verbose_name=_("Applicant"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('City'))
    phone = models.CharField(max_length=135,  verbose_name=_('Phone Number'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('Email'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('Apply Position'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('Birthplace'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('Gender'))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('Profile Picture'))
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=_('Resume Attachment'))

    # School and education information
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_('Bachelor School'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_('Master School'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'PhD School')
    major = models.CharField(max_length=135, blank=True, verbose_name=_('Major'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_('Degree'))
    created_date = models.DateTimeField(verbose_name="Created Date", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)

    # Candidate self-introduction, work experience, project experience
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'Self Introduction')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'Work Experience')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'Project Experience')

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resume List')
    
    def __str__(self):
        return self.username

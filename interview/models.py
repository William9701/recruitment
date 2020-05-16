from django.db import models
from django.contrib.auth.models import User

from jobs.models import DEGREE_TYPE

# First round interview results
FIRST_INTERVIEW_RESULT_TYPE = ((u'Recommend 2nd Round', u'Recommend 2nd Round'), (u'Pending', u'Pending'), (u'Reject', u'Reject'))

# Interview result recommendations
INTERVIEW_RESULT_TYPE = ((u'Recommend Hire', u'Recommend Hire'), (u'Pending', u'Pending'), (u'Reject', u'Reject'))


# HR final interview conclusion
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))


class Candidate(models.Model):
    # Basic information
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'Candidate ID')
    username = models.CharField(max_length=135, verbose_name=u'Name')
    city = models.CharField(max_length=135, verbose_name=u'City')
    phone = models.CharField(max_length=135, verbose_name=u'Phone Number')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'Email')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'Apply Position')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'Birthplace')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'Gender')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Candidate Remark')

    # School and education information
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'Bachelor School')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'Master School')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'PhD School')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'Major')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'Degree')

    # General ability test score, written test score
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name=u'General Ability Test Score')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'Written Test Score')

    # First round interview record
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'First Interview Score',
                                      help_text=u'1-5 scale, Excellent: >=4.5, Good: 4-4.4, Fair: 3.5-3.9, Average: 3-3.4, Poor: <3')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'Learning Ability Score')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name=u'Professional Competency Score')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantages')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Concerns and Weaknesses')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'First Interview Result')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'Recommended Department')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name=u'Interviewer')

    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'First Interview Remark')

    # Second round interview record
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Second Interview Score',
                                       help_text=u'1-5 scale, Excellent: >=4.5, Good: 4-4.4, Fair: 3.5-3.9, Average: 3-3.4, Poor: <3')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name=u'Learning Ability Score')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name=u'Professional Competency Score')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name=u'Pursuit of Excellence Score')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name=u'Communication Ability Score')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name=u'Pressure Resistance Score')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantages')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Concerns and Weaknesses')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'Second Interview Result')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'Recommended Direction or Department')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name=u'Second Interviewer')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Second Interview Remark')

    # HR final interview
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Overall Rating')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Responsibility')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name=u'HR Communication')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Logical Thinking')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Development Potential')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Stability')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantages')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Concerns and Weaknesses')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'HR Interview Result')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name=u'HR Interviewer')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'HR Interview Remark')

    creator = models.CharField(max_length=256, blank=True, verbose_name=u'Creator')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Created Date')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'Modified Date')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'Last Editor')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'Candidate'
        verbose_name_plural = u'Candidates'

        permissions = [
            ("export", "Can export candidate list"),
            ("notify", "notify interviewer for candidate review"),
        ]

    # Python 2 uses this method to convert object to string; if __unicode__() is not available, uses __str__()
    def __unicode__(self):
        return self.username

    # Python 3 directly defines __str__() method, which the system uses to convert object to string
    def __str__(self):
        return self.username
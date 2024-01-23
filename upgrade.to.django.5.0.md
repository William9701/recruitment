# Upgrade to Django 5.0

## Upgrade Dependencies

```bash
pip install --upgrade django django-simple-captcha django-registration-redux django-grappelli django-celery-beat django-bootstrap4 django-prometheus prometheus-client djangorestframework django-celery-beat celery flower django-debug-toolbar django-python3-ldap ldap3 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

If you encounter version issues, check the `requirements.django5.txt` file for Django 5.0 compatible package versions.

## Migrate Celery Database

```bash
python manage.py migrate
```

## Change Admin User Password (Optional)

```bash
python manage.py changepassword admin
```

## Update jobs/template/base.html

Find the following line:

```html
<a href="/accounts/logout" style="text-decoration: none; color:#007bff">{% translate "Logout" %}</a>
```

Replace it with:

```html
<form method="post" action="/accounts/logout/">
  {% csrf_token %}<button type="submit" style="background: none!important;border: none;padding: 0!important;color: #069;text-decoration: underline;cursor: pointer;margin-right: 10px;">{% translate "Logout" %}</button>
</form>
```

## Start the Service

```bash
python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.local
```

## Using the System

- Candidate resume submission: http://127.0.0.1:8000/
- Admin backend: http://127.0.0.1:8000/admin/

**Workflow:**
1. Candidates register and submit resumes
2. Admin marks candidates as "entered process" in the resume list
3. Candidates then appear in the applicant list
4. Admin can assign interviewers and proceed with the interview process

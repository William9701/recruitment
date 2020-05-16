# Django Recruitment Management System

An open-source recruitment and interview management system built with Django & Python, ready to use for startup companies to manage job postings, resume submissions, and recruitment processes.

## Project Overview

A recruitment management system developed with Python Django that can meet the recruitment management needs of different enterprises. Originally built in just two days and gradually improved over time.

### Key Features
- Enterprise domain account integration (LDAP/Active Directory)
- Job posting management
- Resume submission by candidates
- Interview process evaluation
- Candidate data import/export
- DingTalk integration for interview notifications

## Blog

For detailed technical insights, visit: [Ruogue Tech Blog](https://blog.ruoguedu.com/)

## Screenshots

### Recruitment Backend - Home Page
![Recruitment Backend - Home Page](snapshot/recruitment_home_page.png)

### Recruitment Backend - Candidate List
![Recruitment Backend - Candidate List](snapshot/recruitment_candidate_list.png)

### Recruitment Backend - Candidate Evaluation
![Recruitment Backend - Candidate Evaluation](snapshot/recruitment_candidate_evaluation.png)

### Public Recruitment Site - Job List
![Public Recruitment Site - Job List](snapshot/recruitment_job_list_for_candidates.png)

### Public Recruitment Site - Apply for Job
![Public Recruitment Site - Apply for Job](snapshot/recruitment_apply_job.png)

## Prerequisites

Python and Django must be installed on your machine. For more information, visit:
https://docs.djangoproject.com/

## How to Run

For local and production environments, run the following commands respectively:
* Local: `python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.local`
* Production: `python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.production`

Access the application through:
* http://127.0.0.1:8000 - Home page
* http://127.0.0.1:8000/admin - Admin backend

## Import Candidates via Command Line

```bash
python3 manage.py import_candidates --path /path/to/your/file.csv
```

## OpenLDAP/Active Directory Integration

1. Configure LDAP mapping information in `settings/base.py` (accounts created automatically on login will have `is_staff = false` by default)
2. Run `./manage.py ldap_sync_users` to sync LDAP accounts to Django account database
3. Admin logs into backend, edits user properties:
   - Set `is_staff` to true (allows user to login)
   - Add user to the `interviewer` group (grants interview operation permissions)

## DingTalk Notification Integration

Configure the group robot webhook in `settings/local.py` or `settings/production.py`:
```python
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xsxxx"
```

## Sentry Integration

Install sentry-sdk:
```bash
pip install --upgrade sentry-sdk
```

Add Sentry initialization in `settings/local.py` and `settings/production.py`:
```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="http://xxx@recruit.xxxx.com:9000/2",
    integrations=[DjangoIntegration()],
    # Performance tracing sample rate (reduce in production for high traffic)
    traces_sample_rate=1.0,

    # Associate users to errors (requires django.contrib.auth)
    send_default_pii=True
)
```

## Celery Integration

Install Redis and Celery:
```bash
# On macOS
brew install redis

# On Ubuntu/Debian
sudo apt-get install redis

# Install Celery packages
pip install -U celery
pip install "celery[redis,auth,msgpack]"
pip install -U flower
```

Add Celery configuration to `local.py` and `production.py`:
```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")
```

Start local Celery async task service & Flower monitoring:
```bash
DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment worker -l info
DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment flower
```

Upgrade Celery from 4.x to 5.x:
```bash
celery upgrade settings path/to/settings.py
```

## Core Features

* Job management
* Candidates browse and apply for positions
* Import candidate information
* Interview evaluation and feedback
* Domain account integration (LDAP)

## Advanced Features

* DingTalk notification integration (can also send to WeChat Work/Slack)
* Candidate list filtering and search
* Export candidate data (CSV format)
* Permission control:
  - Different permissions for interviewers and HR
  - Data-level permissions (interviewers see only their assigned candidates)
  - Feature permissions (data export)

## Extended Features

* Notify interviewers for interviews
* View resumes from list page
* Internationalization (i18n)
* Error logging and reporting
* REST API (Django Rest Framework)
* Async and scheduled tasks (Celery integration)

## Run in Docker

Interactive mode:
```bash
docker run -it --rm -p 8000:8000 --entrypoint /bin/sh ihopeit/recruitment-base:0.8
```

Mount local source directory:
```bash
docker run -it --rm -p 8000:8000 -v "$(pwd)":/data/recruitment --entrypoint /bin/sh ihopeit/recruitment-base:0.8
```

Load source code with environment variables:
```bash
docker run --rm -p 8000:8000 -v "$(pwd)":/data/recruitment --env server_params="--settings=settings.local" ihopeit/recruitment-base:0.8
```

## License

[View LICENSE file](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

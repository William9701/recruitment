# Integration with Existing System Database

## Scenario

* Provide functionality to browse specified tables in an existing database
* Disable data modification, addition, and deletion operations

## Usage

### Register the app in settings/local.py

```python
INSTALLED_APPS = [
    'running',
] + INSTALLED_APPS
```

### Configure database and database router

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'running': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'running',
        'USER': 'recruitment',
        'PASSWORD': 'recruitment',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['settings.router.DatabaseRouter']
```

### Generate models from existing database

```bash
python manage.py inspectdb --database=running --settings=settings.local area city country province >> running/models.py
```

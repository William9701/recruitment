# When starting the recruitment package, __init__.py will be executed
# __init__.py initializes Django configuration
DJANGO_SETTINGS_MODULE=settings.production celery -A recruitment worker -l INFO


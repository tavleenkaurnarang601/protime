import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_time_tracker.settings')
application=get_wsgi_application()
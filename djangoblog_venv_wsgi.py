import os
import sys

path = 'djangoblog/'
if path not in sys.path
    sys.path.append(path)

os.environ['DJANGO_SETTING_MODULE'] = 'djangoblog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import os
import sys
#
## assuming your django settings file is at '/home/pollyolly/mysite/mysite/settings.py'
## and your manage.py is is at '/home/pollyolly/mysite/manage.py'
path = '/home/pollyolly/djangoblog'
if path not in sys.path:
    sys.path.insert(0, path)
    # sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoblog.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

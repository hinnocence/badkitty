import os
import django.core.handlers.wsgi
import sys
import sae
sys.path.append('badkitty')

os.environ['DJANGO_SETTINGS_MODULE'] = 'badkitty.settings'

application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())

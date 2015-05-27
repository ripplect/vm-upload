"""
WSGI config for upload project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys 

sys.path.append('/home/ripplect_gmail_com/src/upload')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "upload.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'upload.settings'

application = get_wsgi_application()

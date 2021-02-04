"""
WSGI config for Online_shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('MARKET_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_shop.settings.%s' % profile)

application = get_wsgi_application()

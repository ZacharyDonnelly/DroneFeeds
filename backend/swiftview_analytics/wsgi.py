"""
WSGI config for swiftview_analytics project.
"""
# isort:skip
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiftview_analytics.settings')

from django.core.wsgi import get_wsgi_application  # isort:skip

application = get_wsgi_application()

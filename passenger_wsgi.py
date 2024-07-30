# import imp
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))
# sys.setrecursionlimit(10000)  # Set the recursion limit to a higher value

# wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# application = wsgi.application


import os
import sys

# Add your Django project's root directory to the Python path
sys.path.append('/home/rbtszbja/px_g/')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pax.settings')

# Import the Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
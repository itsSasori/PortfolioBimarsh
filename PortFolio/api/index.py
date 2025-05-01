import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PortFolio.settings")

app = get_wsgi_application()

# This file is used by Vercel to run Django as a serverless function

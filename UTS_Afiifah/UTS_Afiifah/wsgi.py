"""
WSGI config for UTS_Afiifah project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UTS_Afiifah.settings')

application = get_wsgi_application()

# Tambahkan baris ini di paling bawah agar dibaca Vercel
app = application

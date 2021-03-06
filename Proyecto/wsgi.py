"""
WSGI config for Proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys

#path a donde esta el manage.py de nuestro proyecto Django
sys.path.append('Users/David/EnMovimiento')

#referencia (en python) desde el path anterior al fichero settings.py
#Importante hacerlo así, si hay varias instancias coriendo (en lugar de setdefault)
os.environ['DJANGO_SETTINGS_MODULE'] = "proyectodjango.settings"
#os.environ.setdefault(“DJANGO_SETTINGS_MODULE”, “proyectodjango.settings”)

#prevenimos UnicodeEncodeError
os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

#activamos nuestro virtualenv
activate_this = "pathToVirtualenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

#obtenemos la aplicación
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

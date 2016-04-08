from django.conf import settings

STATIC_URL = '{0}md/'.format(settings.STATIC_URL)
HELP_URL = '{0}md/html/mdhelp.html'.format(settings.STATIC_URL)

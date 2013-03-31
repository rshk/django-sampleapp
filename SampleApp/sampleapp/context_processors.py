"""
:author: samu
:created: 3/31/13 6:10 PM
"""
from django.conf import settings


def site_info(request):
    return {
        'SITE_TITLE': settings.SITE_TITLE,
    }

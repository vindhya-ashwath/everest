# -*- coding: utf-8 -*-

from .common import *  # noqa

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


def show_toolbar(request):
    return False
    # return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

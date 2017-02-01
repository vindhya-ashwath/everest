from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [

    ################################################
    # Login URLs                                   #
    ################################################
    url(r'^(?P<ver>[\w\.]+)/auth$',
        view=obtain_jwt_token
        ),

    ################################################
    # Deal URLs                                   #
    ################################################
    url(r'^(?P<ver>[\w\.]+)/deals/(?P<deal_id>[0-9])$',
        view=obtain_jwt_token
        ),
]

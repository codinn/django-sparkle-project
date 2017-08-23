from django.conf.urls import url, include
from sparkle.views import appcast

urlpatterns = [
    url(r'^(?P<application_id>\d+)/appcast.xml$', appcast, name='sparkle_application_appcast'),
]

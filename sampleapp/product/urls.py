from django.urls import path, include
from django.conf.urls import url
from .versions.v1 import urls as v1_urls


urlpatterns = [
    path('v1/', include(v1_urls)),
]
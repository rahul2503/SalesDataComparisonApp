from django.urls import path, include
from django.conf.urls import url
from .versions.v1 import urls as v1_urls


urlpatterns = [
    path('product/', include(v1_urls)),
]
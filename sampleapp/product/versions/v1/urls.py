from django.conf.urls import url
from django.urls import path
from .views import SaleCompareView

urlpatterns = [
    path('v1/sale_compare', SaleCompareView.as_view(), name='sale_compare'),
]

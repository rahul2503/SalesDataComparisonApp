from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from django.db.models.functions import ExtractWeek


from product.models import Product, Sale
from datetime import datetime


class SaleCompareView(APIView):
	def get(self, request):
		product_id = request.query_params['product_id']

		today = datetime.now()
		weekday = today.weekday()
		avg_current_week_sale = Sale.objects.filter(id__in=Sale.objects.prefetch_related('product').filter(product=Product.objects.get(id=product_id)).values_list('id', flat=True),
													year_id=today.year, 
													month_id=today.month, 
													day_id__gt=today.day-weekday).aggregate(Avg('total_sale'))['total_sale__avg']

		weekly_sale_avg = Sale.objects.values('week_id').annotate(weekly_sale=Avg('total_sale')).aggregate(Avg('weekly_sale'))['weekly_sale__avg']
		difference = weekly_sale_avg - avg_current_week_sale

		return Response({"difference": round(difference, 2)})

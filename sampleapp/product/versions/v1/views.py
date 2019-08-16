from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg

from product.models import Product, Sale
from product.helpers import calculate_weekly_avg_sale
from datetime import datetime


class SaleCompareView(APIView):
	
	def get(self, request):
		today = datetime.now()
		weekday = today.weekday()
		avg_current_week_sale = Sale.objects.filter(year_id=today.year, month_id=today.month, day_id__gt=today.day-weekday).aggregate(Avg('total_sale'))


		avg_all_weeks_sale = calculate_weekly_avg_sale(number_of_weeks=52)

		return Response({"aaa": "bbb"})
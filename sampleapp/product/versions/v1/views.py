from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Q
from django.db.models.functions import ExtractWeek
from rest_framework import status

from product.models import Product, Sale
from datetime import datetime, timedelta


class SaleCompareView(APIView):
	def get(self, request):
		product_id = request.query_params['product_id']

		today = datetime.now()
		weekday = today.weekday()

		current_week = Sale.objects.filter(updated_at__date=(datetime.now().date())).annotate(week=ExtractWeek('updated_at')).values_list('week', flat=True)
		if len(current_week) != 0:
			sale_ids = Sale.objects.prefetch_related('product').filter(product__id=product_id).values_list('id', flat=True)
			avg_current_week_sale = Sale.objects.filter(id__in=sale_ids, week_id=current_week[0]).aggregate(Avg('total_sale'))['total_sale__avg']

			# last week of year
			if current_week[0] == 52:
				weekly_sale_avg = Sale.objects.filter(
													Q(id__in=sale_ids), 
													Q(week_id__range=(1, current_week[0]), year_id=today.year)) \
												.values('week_id') \
												.annotate(weekly_sale=Avg('total_sale')) \
												.aggregate(Avg('weekly_sale'))['weekly_sale__avg']
			else:
				weekly_sale_avg = Sale.objects.filter(
													Q(id__in=sale_ids), 
													Q(week_id__range=(1, current_week[0]), year_id=today.year) |
													Q(week_id__range=(current_week[0]+1, 52), year_id=today.year-1)) \
												.values('week_id') \
												.annotate(weekly_sale=Avg('total_sale')) \
												.aggregate(Avg('weekly_sale'))['weekly_sale__avg']

			difference = weekly_sale_avg - avg_current_week_sale
			return Response({"difference": round(difference, 2)}, status=status.HTTP_200_OK)
		else:
			return Response({"error": {"message": "No data for current week"}}, status=status.HTTP_200_OK)

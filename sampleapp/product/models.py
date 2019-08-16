from django.db import models

# Create your models here.
class BaseTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True


class Product(BaseTimeStamp):
	name = models.CharField(max_length=50)
	description = models.TextField()

	class Meta(object):
		db_table = 'product'
		verbose_name_plural = 'products'


class Sale(BaseTimeStamp):
	product = models.ManyToManyField(Product, related_name='orders')
	quantity = models.PositiveIntegerField()
	price_each = models.DecimalField(max_digits=6, decimal_places=2)
	total_sale = models.DecimalField(max_digits=10, decimal_places=2)
	day_id = models.PositiveSmallIntegerField()
	month_id = models.PositiveSmallIntegerField()
	year_id = models.PositiveSmallIntegerField()

	class Meta(object):
		db_table = 'sale'
		verbose_name_plural = 'sales'

import factory  
import factory.django
from faker import Faker
from datetime import datetime
from decimal import *

from .models import Product, Sale


fake = Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = fake.name()
    description = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)


class SaleFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Sale

	quantity = fake.numerify()
	price_each = fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=1, max_value=500)
	total_sale = Decimal(quantity) * Decimal(price_each)
	day_id = int(fake.day_of_month())
	week_id = int(fake.day_of_month())
	month_id = int(fake.month())
	year_id = 2018 if (month_id > (datetime.now().month - 1)) else 2019

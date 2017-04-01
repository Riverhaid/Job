from background_task import background
from django.apps import apps
from common.util.parser import *
from django.db import transaction

@background(schedule=0)
def data_pars():
	products = do_it()
	print("Продукты получили, добавляем ", products)
	with transaction.atomic():
		Product = apps.get_model('polls', 'Product')
		Category = apps.get_model('polls', 'Category')

		for product in products:
			print("Добавление ", product['name'])
			print(product['price'])
			prd, created = Product.objects.get_or_create(slug=product['product_id'])
			prd.name = product['name']
			prd.slug = product['product_id']
			prd.price = float(product['price'][0])
			prd.description = product['options']
			prd.color = product['colors']
			ctr, created = Category.objects.get_or_create(name=product['category'])
			prd.category = ctr
			prd.save()

		print("Конец")

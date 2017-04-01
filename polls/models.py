from django.db import models
from django.utils.safestring import mark_safe
from datetime import *
import os
from job import settings
from django.core.urlresolvers import reverse
# Create your models here.

			
class Category(models.Model):
    name = models.CharField(max_length=200, null=True, db_index=True)
    slug = models.SlugField(max_length=200, null=True, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('polls:ProductListByCategory', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, verbose_name="Категория")
    name = models.CharField(max_length=200, null=True, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, null=True, db_index=True)
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, null=True, decimal_places=2, verbose_name="Цена")
    color = models.TextField(blank=True, null=True, verbose_name="Цвета")
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
          return reverse('polls:ProductDetail', args=[self.id, self.slug])

   
          	
class Request(models.Model):
	"""docstring for ClassName"""
	CategoryID=models.ForeignKey(Category)
	ProductID=models.ForeignKey(Product)
	Date = models.DateTimeField(verbose_name="Date")
	class Meta:
		verbose_name= "Request"
		verbose_name_plural="Requests"
	def __str__(self):
		return 'Request %s' % self.Date
	
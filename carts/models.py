from django.db import models
from products.models import Product
# Create your models here.

class CartItem(models.Model):
	#cart foreign key
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title

class Cart(models.Model):
	items = models.ManyToManyField(CartItem, null=True, blank=True)
	products = models.ManyToManyField(Product, null = True, blank = True)
	total = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Cart id: %s" %(self.id)
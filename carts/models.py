from django.db import models
from products.models import Product
# Create your models here.

class CartItem(models.Model):
	#cart foreign key
	cart = models.ForeignKey('Cart', null=True, blank=True,on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(max_digits=1000,default=10.99, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title

class Cart(models.Model):
	# items = models.ManyToManyField(CartItem, null=True, blank=True)
	# products = models.ManyToManyField(Product, null = True, blank = True)
	total = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Cart id: %s" %(self.id)


from django.contrib.auth.models import User
from django.db import models


class StaffRole(models.Model):
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class Staff(models.Model):
	role = models.ForeignKey('StaffRole', on_delete=models.PROTECT, null=True)
	name = models.CharField(max_length=255)

class Table(models.Model):
	@property
	def total_sum(self):
		result: int = 0
		for item in self.orders.all():
			result += item.sum
			a = result * 0.15
			b = result + a
		return b			

class Order(models.Model):
	table = models.ForeignKey("Table", related_name="orders", on_delete=models.CASCADE, null=True)

	food = models.ForeignKey('Food',on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField()
	user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

	@property
	def sum(self) :
		return self.quantity * self.food.price

class Food(models.Model):
	title = models.CharField(max_length=50)
	price = models.IntegerField(default=300)
	def __str__(self):
		return self.title

class Quantity(models.Model):
	quantity = models.IntegerField(default=2)
	food = models.ForeignKey('Food', on_delete=models.CASCADE, null=True)

class Percent(models.Model):
	percent = models.IntegerField(default=15)



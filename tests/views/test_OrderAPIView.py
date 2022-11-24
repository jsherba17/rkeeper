from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from cafe.models import Food, Order, Table


class OrderAPIViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create()
		cls.food = Food.objects.create(title='Pizza', price=100)
		cls.order = Order.objects.create(user=cls.user, food=cls.food, quantity=2)


	def setUp(self) -> None:
		self.client = APIClient()
		self.url = reverse('order')

	def test_get_order(self):
		response = self.client.get(self.url)
		self.assertTrue(response.data)
		self.assertEqual(response.status_code, 200)

	def test_post_order(self):
		data = {
			'food': self.food.pk,
			'quantity': 3,
			'user': self.user.pk
		}
		response = self.client.post(self.url, data)
		self.assertTrue(Order.objects.filter(quantity=3).exists())
		self.assertEqual(response.status_code, 201)



	def test_total_sum(self):
		food = Food.objects.create(title='Ice Cream', price=200)
		food1 = Food.objects.create(title='Burger', price=100)
		table = Table.objects.create()
		user = User.objects.create(username='tester')
		order = Order.objects.create(food=food,quantity=2, table=table,user=user)
		order1 = Order.objects.create(food=food1, quantity=3, table=table, user=user)
		response = self.client.get(reverse('tables'))
		self.assertTrue(len(response.data) == 1)
		response_data = response.data[0]
		a = food.price * order.quantity
		b = food1.price * order1.quantity
		c = (a+b) * 0.15
		self.assertEqual(response_data['total_sum'], (a+b)+c)

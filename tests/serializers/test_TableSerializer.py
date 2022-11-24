from django.contrib.auth.models import User
from django.test import TestCase

from cafe.models import Table, Order
from cafe.serializers import TableSerializer


class TableSerializerTest(TestCase):
	def test_table_serializer(self):
		table = Table.objects.create()
		order = Order.objects.create(quantity=1, user=User.objects.create(), table=table)
		r = TableSerializer(table).data
		self.assertTrue(r['percent'])

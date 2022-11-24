from rest_framework import serializers
from cafe.models import *

class PercentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Percent
		fields = ['percent']

class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = ['name']

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['food','quantity','sum','user']


class TableSerializer(serializers.ModelSerializer):
	orders = OrderSerializer(many=True)
	percent = serializers.SerializerMethodField()

	class Meta:
		model = Table
		fields = ['total_sum', 'orders','percent']

	def get_percent(self, obj):
		instance, _ = Percent.objects.get_or_create()
		return instance.percent


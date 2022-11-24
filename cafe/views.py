from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from cafe.serializers import *


class OrderAPIView(APIView):

    def get(self, request):
        o = Order.objects.all()
        return Response({'posts': OrderSerializer(o, many=True).data}, status=200)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'posts': serializer.data}, status=201)

class TableAPIView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

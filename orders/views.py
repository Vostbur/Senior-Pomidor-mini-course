from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def index(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, 'orders.html')

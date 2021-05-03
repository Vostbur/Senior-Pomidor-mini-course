from django.urls import path
from rest_framework.routers import SimpleRouter

from orders.views import index, OrderView, orders_app

router = SimpleRouter()
router.register('api/orders', OrderView)

urlpatterns = [
    path('', index),
    path('orders/', orders_app)
]

urlpatterns += router.urls

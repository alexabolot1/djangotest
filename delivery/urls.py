from django.urls import path, include

from delivery.views import DeliveryList, DeliveryCreate

app_name = 'delivery'

urlpatterns = [
    path('', DeliveryList.as_view(), name='delivery_list'),
    path('delivery_create/', DeliveryCreate.as_view(), name='delivery_create')
]

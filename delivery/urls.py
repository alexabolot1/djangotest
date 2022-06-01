from django.urls import path

from delivery.views import DeliveryList, DeliveryCreate, index

app_name = 'delivery'

urlpatterns = [
    path('', index, name='index'),
    path('delivery_list/', DeliveryList.as_view(), name='delivery_list'),
    path('delivery_create/', DeliveryCreate.as_view(), name='delivery_create')
]

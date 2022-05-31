from django.contrib import admin

# Register your models here.
from delivery.models import ProductType, Delivery, DeliveryPoint

admin.site.register(ProductType)
admin.site.register(Delivery)
admin.site.register(DeliveryPoint)

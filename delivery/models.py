from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=128, verbose_name='тип продукта')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'


class DeliveryPoint(models.Model):
    address = models.TextField(max_length=128, verbose_name='адрес')
    description = models.TextField(blank=True, null=True, verbose_name='описание пункта выдачи')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='активен')

    def __str__(self):
        return f'{self.address}'


class Delivery(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='название товара')
    product_type = models.ForeignKey(ProductType, on_delete=models.SET, verbose_name='тип товара')
    delivery_date = models.DateField(blank=True, verbose_name='дата доставки')
    file = models.FileField(upload_to='delivery_files', verbose_name='файл')
    point = models.ForeignKey(DeliveryPoint, on_delete=models.SET, verbose_name='пункт выдачи')

    def __str__(self):
        return f'Доставка № {self.id}'

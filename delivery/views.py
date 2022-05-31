from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.forms import formset_factory

from delivery.forms import DeliveryForm
from delivery.models import Delivery


class DeliveryList(ListView):
    model = Delivery
    template_name = 'index.html'


class DeliveryCreate(CreateView):
    form_class = DeliveryForm
    template_name = 'delivery_create.html'
    success_url = reverse_lazy('delivery:delivery_list')


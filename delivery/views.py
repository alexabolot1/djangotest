from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from delivery.forms import DeliveryForm
from delivery.models import Delivery


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'delivery/index.html', context)


class DeliveryList(ListView):
    model = Delivery
    template_name = 'delivery/delivery_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список доставок'
        return context


class DeliveryCreate(CreateView):
    form_class = DeliveryForm
    template_name = 'delivery/delivery_create.html'
    success_url = reverse_lazy('delivery:delivery_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание доставки'
        return context

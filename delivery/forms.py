from django import forms
from django.forms.widgets import DateInput
from delivery.models import Delivery


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
        widgets = {
            'delivery_date': DateInput(attrs={'type': 'date'})
        }

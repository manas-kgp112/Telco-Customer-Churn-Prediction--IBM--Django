from django.forms import ModelForm
from .models import CustomerData


class getCustomerData(ModelForm):
    class Meta:
        model = CustomerData
        fields = '__all__'
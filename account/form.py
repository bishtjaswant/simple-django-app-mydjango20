from django import forms
from account.models import Order,Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields ='__all__'





class CustomerForm(forms.ModelForm):
    class Meta:
        model  =  Customer
        fields = '__all__'

        # widgets = {
        #     'name' : forms.CharField(  attr={ 'class':'form-control'   } ),
        # }




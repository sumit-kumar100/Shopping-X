from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from .models import Address, Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class RegistrationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.EmailInput(),
        label='Email'
    ) 
    class Meta:
        model = User
        fields = ['first_name','last_name','username']





class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.EmailInput(attrs={'class':'myuser'}),
        label='Email'
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'mypass'})
    )



# Address Form
class AddressForm(forms.ModelForm):
    phone_no = PhoneNumberField(
        # widget=PhoneNumberPrefixWidget(initial='IN')
    )
    class Meta:
        model = Address
        fields = ['name','locality','state','zipcode','phone_no']



# Checkout form
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
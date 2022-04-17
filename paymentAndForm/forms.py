from django import forms
from paymentAndForm.models import Customers
from captcha.fields import CaptchaField

class CustomenrsFrom(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Customers
        fields = ['name', 'lastname', 'address', 'phone', 'email']
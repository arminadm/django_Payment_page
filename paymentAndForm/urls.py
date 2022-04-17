from django.urls import path
from paymentAndForm.views import *

app_name = 'paymentAndForm'

urlpatterns = [
    path('', form_view, name='form')
]

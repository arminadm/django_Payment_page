from django.urls import path
from paymentAndForm.views import *

urlpatterns = [
    path('', form_view, name='form')
]

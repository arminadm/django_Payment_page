from django.contrib import admin
from paymentAndForm.models import Customers
# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['name', 'lastname', 'email', 'payment', 'created_date']
    list_filter = ('email','payment')
    search_fields = ['name', 'lastname', 'email', 'phone']
admin.site.register(Customers, CustomersAdmin)
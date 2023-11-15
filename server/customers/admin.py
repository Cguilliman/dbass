from django.contrib import admin
from customers.models import Customer


admin.site.register(Customer, list_display=("name", "birthday"))

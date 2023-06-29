from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Currency, Money 


admin.site.register(Currency)
admin.site.register(Money)
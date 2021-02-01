from django.contrib import admin
from .models import Item, UserRegistration, CharityRegistration, OrderedItem

# Register your models here.
admin.site.register(Item)
admin.site.register(UserRegistration)
admin.site.register(CharityRegistration)
admin.site.register(OrderedItem)

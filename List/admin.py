from django.contrib import admin

from List.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Supermarket)
admin.site.register(Product)
admin.site.register(HistoricalPrice)
admin.site.register(List)
admin.site.register(ProductsList)
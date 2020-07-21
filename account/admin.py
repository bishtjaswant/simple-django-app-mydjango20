from django.contrib import admin
from .models import Customer,Product,Order,Tag


#CUStmer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

#order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass



#tag
@admin.register(Tag)
class ProductAdmin(admin.ModelAdmin):
    pass

#product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

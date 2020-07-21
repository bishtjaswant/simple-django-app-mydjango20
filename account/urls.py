from django.urls import path
from .views import Index,Profile,Product,customer,createOrder,updateOrder,createCustomer,updateCustomer, deleteOrder, deleteCustomer

urlpatterns =[
    path('',Index,name='home'),
    path('products/',Product.as_view(),name='product'),
    path('customer/<int:pk>',customer,name='customer' ),
    path('profile/',Profile.as_view(),name='profile'),


    # create order by customer
    path('create_order/<int:cid>',createOrder,name='create_order'),
    path('update_order/<int:pk>',updateOrder,name='update_order'),
    # delete order
    path('delete_order/<int:pk>',deleteOrder,name='delete_order'),



   # create customer
    path('create_customer/',createCustomer,name='create_customer'),
   # update customer
    path('update_customer/<int:pk>',updateCustomer,name='update_customer'),
   # delete customer
    path('delete_customer/<int:pk>',deleteCustomer,name='delete_customer'),


]
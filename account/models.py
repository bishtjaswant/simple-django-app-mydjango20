from django.db import models



# customer
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=15,null=True)
    date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customers'






# tags
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return  self.name

    class Meta:
        db_table ='tags'



# product
class Product(models.Model):
    product_category = (
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    price = models.FloatField(null=True)
    category= models.CharField(null=True,max_length=255,choices=product_category)
    description = models.TextField(null=True)
    tag = models.ManyToManyField(Tag)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'

# 238sheri

#orders
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_status = (
        ('pending','pending'),
        ('out 4 delivery','out 4 delivery'),
        ('delivered','delivered'),
    )
    product= models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    customer=  models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    status = models.CharField(null=True,max_length=255,choices=order_status)
    date =models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'orders'




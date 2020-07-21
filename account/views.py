from django.shortcuts import render
from django.shortcuts import redirect
from  django.http import Http404
from django.views import View
from django.views.generic import ListView,DetailView
from  account.models import Product,Customer,Order
from account.form import OrderForm,CustomerForm
from django.forms import  inlineformset_factory



def Index(request):
    template= 'account/index.html'
    customers= Customer.objects.all()
    orders = Order.objects.all()
    total_ordered = Order.objects.count()
    total_pending = Order.objects.filter(status='pending').count()
    total_delivered = Order.objects.filter(status='pending').count()
    context = {
        'customers':customers,
        'orders':orders,
        'total_pending':total_pending,
        'total_ordered':total_ordered,
        'total_delivered':total_delivered,
    }
    return render(request,template, context)


def customer(request,pk):
    if request.method=='GET':
        customer=  Customer.objects.get(id=pk)
        order= customer.order_set.all()
        order_count= order.count()
        context ={}
        context['customer']=customer
        context['orders']=order
        context['order_count']=order_count
        return render(request,"account/customer.html",context)


def createCustomer(request) :
    form = CustomerForm()
    context = {}
    context['form'] = form

    if request.method=='POST':
        form= CustomerForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'account/customer_form.html',context)


# delete customer
def deleteCustomer(req,pk):
    instance = Customer.objects.get(id=pk)
    if req.method == 'POST':
        instance.delete()
        return redirect('home')
    context = {}
    context['customer'] = instance
    return render(req, 'account/delete_customer.html', context)


def updateCustomer(request,pk ) :
    instance = Customer.objects.get(id=pk)
    form = CustomerForm(instance=instance)
    print(instance.id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {}
    context['form'] = form
    context['id'] =instance.id
    return render(request,'account/customer_form.html', context   )




# class Customer(DetailView):
#     template_name =  'account/customer.html'
#     context_object_name = 'customer';
#     model = Customer
#
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(Customer,
#                         self).get_context_data(*args, **kwargs)
#         # add extra field
#         context["order"] = 'ok'
#         return context



class Product(ListView):
    template_name = 'account/product.html'
    model = Product
    context_object_name = 'all_products'

    # def get(self,request):
    #     return render(request,self.template)



class Profile(View):
    template = 'account/profile.html'
    def get(self,request):
        return render(request,self.template)




# CREATE ORDER by customer
def createOrder(req,cid):

    customer= Customer.objects.get(id=cid)
    inlineform =inlineformset_factory(Customer,Order,fields=('product','customer','status'))
    form= inlineform(instance=customer)
    if req.method=="POST":
        # print(req.POST)
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
    context={}
    context['formset']= form
    context['id']=customer.id
    return render(req, 'account/order_form.html',context);


# update order
def updateOrder(req,pk):
    instance =Order.objects.get(id=pk)
    form = OrderForm(instance=instance)
    if req.method=="POST":
        form = OrderForm(req.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={}
    context['form'] = form
    context['id'] = instance.id
    return render(req,'account/order_form.html',context)

# delete order
def deleteOrder(req,pk):

    instance=Order.objects.get(id=pk)
    if req.method=='POST':
        instance.delete()
        return redirect('home')
    context={}
    context['item']=instance
    return  render(req,'account/delete_order.html',context)





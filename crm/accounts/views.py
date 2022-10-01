from math import prod
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def dashboard(request):
  orders = Order.objects.all()
  customers = Customer.objects.all()

  total_orders = orders.count()
  delivered = orders.filter(status='Delivered').count()
  pending = orders.filter(status='Pending').count()

  context = {'orders':orders, 'customers':customers,
  'total_orders':total_orders,
  'delivered':delivered,
  'pending':pending}
  template = 'accounts/dashboard.html'
  return render(request, template, context)


def customer(request, pk):
  customer = Customer.objects.get(id=pk)
  orders = customer.order_set.all()
  order_count = orders.count()
  context = {
    'customer':customer,
    'orders':orders,
    'order_count':order_count
  }
  return render(request, 'accounts/customer.html', context)


def products(request):
  products = Product.objects.all()
  context = {
    'products': products
  }
  template = 'accounts/products.html'

  return render(request, template, context)

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Product
from django.db.models import Q
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

def client_orders(request, client_id):
    orders = Order.objects.filter(client_id=client_id).prefetch_related('products')
    return render(request, 'client_orders.html', {'orders': orders})


def client_products(request, client_id, period_days):
    period = timezone.now() - timedelta(days=period_days)
    orders = Order.objects.filter(client_id=client_id, order_date__gte=period)
    products_ids = orders.values_list('products', flat=True).distinct()
    products = Product.objects.filter(id__in=products_ids)
    return render(request, 'client_products.html', {'products': products, 'period_days': period_days})
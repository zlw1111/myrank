from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from rank.models import Myself
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            myself=Myself.objects.get(name='ck')
            total=cart.get_total_price()
            myself.balance=myself.balance-total
            myself.save()
            order = form.save()
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
   
                # clear the cart
            cart.clear()
            return render(request,
                             'orders/order/created.html',
                             {'order': order})
    else:
        form = OrderCreateForm()
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})
def error_paid(request):
    return render(request,
                  'orders/order/error_paid.html',
                  {})
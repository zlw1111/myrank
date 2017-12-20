# -*- coding: utf-8 -*-
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Product, Myself, Comment
from orders.models import Order,OrderItem
from cart.forms import CartAddProductForm
from .forms import CommentCreateForm,MyselfCreateForm
from django.db.models import Q


def product_list(request, restaurant_slug=None):
    restaurant = None
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available=True)
    comments = Comment.objects.all()
    
    if restaurant_slug:
        restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
        products = products.filter(restaurant=restaurant)
    product1 = products.filter(Q(slug__icontains='no1'))[:5]
    product2 = products.filter(Q(slug__icontains='no2'))[:5]
    product3 = products.filter(Q(slug__icontains='no3'))[:5]
    product4 = products.filter(Q(slug__icontains='no4'))[:5]
    product5 = products.filter(Q(slug__icontains='no5'))[:5]
    orderitems = OrderItem.objects.all()
    myproduct = Product.objects.all()
   
    for product in products:
        num=product.grade
        p=Product.objects.get(name=product.name)
        if(orderitems):
            for ordernum in orderitems:
                if ordernum.product.name == product.name:
                    num=num+1
            if num!=0:
                p.grade=num
                p.save()
    order2 = Order.objects.filter(name='ck')
    for pro in myproduct:
        pro.myrank=0
        for order3 in order2:
            myorder = OrderItem.objects.filter(order=order3)
            for items in myorder:
                if items.product.name==pro.name:
                    pro.myrank=pro.myrank+1
        pro.save()
    rank = myproduct.order_by("-myrank")[0:5]
            
    products_rank=Product.objects.order_by("-grade")[0:10]
    return render(request, 
                  'rank/product/list.html', 
                  {'restaurant': restaurant,
                  'restaurants': restaurants,
                  'products': products,
                  'comments': comments,
                  'products_rank':products_rank,
                  'product1':product1,
                  'product2':product2,
                  'product3':product3,
                  'product4':product4,
                  'product5':product5,
                  'myrank':rank,
                  'myorder':myorder,
                  'order':order2})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, 
                                id=id, 
                                slug=slug, 
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 
                  'rank/product/detail.html', 
                  {'product': product,
                   'cart_product_form': cart_product_form})
def show_product(request,restaurant_slug=None):
    product = Product.objects.filter(available=True)
    restaurant = None
    restaurants = Restaurant.objects.order_by("id")
    products = Product.objects.filter(available=True)
    if restaurant_slug:
        restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
        products = products.filter(restaurant=restaurant)
    return render(request,
                  'rank/product/show_product.html',
                  {'product':product,
                   'restaurant':restaurant,
                  'restaurants': restaurants,
                  'products': products,})
def show_me(request):
    myself = Myself.objects.filter(name='ck')
    order = Order.objects.filter(name='ck',paid=False)
    order2 = Order.objects.filter(name='ck',paid=True)[0:10]
    orderitems = OrderItem.objects.all()
    product = Product.objects.all()

    return render(request,
                  'rank/product/show_me.html',
                  {'myself':myself,
                   'orderitems':orderitems,
                   'product':product,
                   'order':order,
                   'order2':order2})
def comment_create(request,product_slug,order_id):
        product=Product.objects.get(slug=product_slug)
        myself = Myself.objects.get(name='ck')
        form = CommentCreateForm(request.POST)
        order=Order.objects.get(id=order_id)
        if request.method == 'POST':
            form = CommentCreateForm(request.POST)
            if form.is_valid():
                  comment1=Comment(product=product,
                                   myself=myself,
                                   des=form['des'],
                                   score=1)
                  order.paid=True
                  order.save()
                  comment1.save()
                  return render(request,
                              'rank/product/commentcreated.html',
                              {})
        else:
            form = CommentCreateForm()
            return render(request,
                                   'rank/product/comment_create.html',
                                   {'form': form,
                                    'product_slug':product_slug,
                                    'order_id':order_id})
        
        

def search(request):
    request.encoding='utf-8'
    q = request.GET.get('q')
    error_msg = ''
    allproduct=Product.objects.all()
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'rank/product/search.html', {'error_msg': error_msg})
    
    post_list = allproduct.filter(Q(name__icontains=q))
    return render(request, 
                  'rank/product/search.html', 
                  {'error_msg': error_msg,
                   'post_list':post_list})
        
        
 
 # Create your views here.

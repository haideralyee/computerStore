from django.shortcuts import render, redirect
from cart.models import Product,Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.session.get('cart'):
        cart=request.session.get('cart') 
    else:
        cart={}
    print(cart.get (str(product_id)))
    cart[product_id] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')



def view_cart(request):
    if request.session.get('cart'):
        cart= request.session.get('cart')
    else:
        cart={}
    product_ids = cart.keys()
    products_in_cart = Product.objects.filter(pk__in=product_ids)
    total_price = sum(product.price * cart[str(product.id)] for product in products_in_cart)
    return render(request, 'cart/view_cart.html', {'cart': cart, 'products_in_cart': products_in_cart, 'total_price': total_price})

def remove_from_cart(request,product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]
    request.session['cart']=cart
    return redirect ('view_cart')


def item_list(request):
    items_list = Item.objects.all()

    # Number of items to display per page
    items_per_page = 1

    # Create a Paginator instance
    paginator = Paginator(items_list, items_per_page)

    # Get the current page number from the request
    page = request.GET.get('page', 1)

    try:
        # Get the items for the requested page
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        items = paginator.page(paginator.num_pages)

    return render(request, 'cart/item_list.html', {'items': items})
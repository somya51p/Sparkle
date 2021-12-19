from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

# def _cart_id(request):
#     cart=request.session.session_key
#     if not cart:
#         cart=request.session.create()
#     return cart

# def add_cart(request, product_id):

def delete_p(request,pid):
    cart = Product.objects.get(id=pid)
    cart.delete()
    return redirect('store')
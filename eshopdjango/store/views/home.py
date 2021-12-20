from django.shortcuts import render , redirect , HttpResponseRedirect
from django.http import Http404
from store.models.product import Product
from store.models.category import Category
from django.views import View
from store.models.customer import Customer
from store.models.orders import Order
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    return render(request, 'index.html', data)


def home(request):
    return render(request, 'home.html')

def profile(request):
    # user = Customer.objects.all().order_by('-id')
    context = {
        'user' : Customer.objects.get(id=2),
        # 'orders' : Order.objects.get(),
    }
    return render(request, 'profile.html', context)

def desc(request):
    return render(request, 'desc.html')
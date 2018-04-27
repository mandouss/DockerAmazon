from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate,login, logout
from goods.models import Good
# Create your views here.

from .models import Cart

def authenticated_view(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return function(request)
        else:
            login_form = LoginForm()
        return render(request, 'auth/login.html', locals())


@authenticated_view
def view_cart(request):
    cart = request.session.get(request.user.id, None)
    return render(request, 'checkout.html', locals())

@authenticated_view
def add_cart(request):
    try:
        gid = request.POST.get('gid, None')
        try:
            good = Good.objects.get(pk=gid)
        except Good.DoesNotExist:
            print("Opooooos")
        cart = request.session.get(request.user.id, None)
        if not cart:
            cart = Cart()
            cart.add(good)
            request.sseion[request.user.id] = cart
        else:
            cart.add(good)
            request.session[request.user.id] = cart
    except Exception as e:
        print("Opooooos, again")
    return render(request, 'checkoutout.html', locals())

@authenticated_view
def cleanCart(request):
    cart = Cart()
    request.session[requet.user.id] = cart
    return render(request, 'checkout.html', locals())

@authenticated_view
def clean_one_item(request, id):
    item = None
    try:
        item = Good.objects.get(pk=id)
    except Good.DoesNotExist:
        pass
    if item:
        item.delete()
        cart = request.session.get(request.user.id, None)
    return render(request, 'checkout.html', {'cart':cart})



# def cart_home(request):
    # cart_obj, new_obj = Cart.objects.new_or_get(request)
    # print(e)
    # return render(request, "carts/home.html", {"cart": cart_obj })


# def cart_update(request):
    # good_id = request.POST.get('good_id')
    # if good_id is not None:
        # try:
            # good_obj = Good.objects.get(id=good_id)
        # except Good.DoesNotExist:
            # print("Show message touser, product is gone?")
            # return redirect("cart:home")
        # cart_obj, new_obj = Cart.objects.new_or_get(request)
        # if good_obj in cart_obj.goods.all(): 
            # cart_obj.goods.remove(good_obj)
        # else:      
            # cart_obj.goods.add(good_obj) #ManyToManyField
        # request.session['cart_items'] = cart_obj.goods.count()
    # return redirect("cart:home")

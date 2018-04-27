from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Good
from .models import Cart, CartItem
from shop.forms import AorderForm
from django.conf import settings
from shop.models import Good, Aorder, Warehouse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, good_id):
    good = Good.objects.get(ID=good_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
                cart_id = _cart_id(request)
                )
        cart.save()
    try:
        cart_item = CartItem.objects.get(good=good, cart=cart)
        cart_item.amount += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                good = good,
                amount = 1,
                cart = cart,
                )
        cart_item.save() 
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += cart_item.amount
            counter += cart_item.amount
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter))


def cart_remove(request, good_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    good = get_object_or_404(Good, ID=good_id)
    cart_item = CartItem.objects.get(good=good, cart=cart)
    if cart_item.amount > 1:
        cart_item.amount -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request, good_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    good = get_object_or_404(Good, ID=good_id)
    cart_item = CartItem.objects.get(good=good, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
  
# Create your views here.:wq

def create_order(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += cart_item.amount
            counter += cart_item.amount
    except ObjectDoesNotExist:
        pass
    aorderform = AorderForm()
    return render(request, 'order.html', dict(aorderform=aorderform, cart_items = cart_items, total = total, counter = counter))

def email(to_email, subject, message):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, to_email, fail_silently=False)

def accept_order(request, cart_items = None):
    form = AorderForm(request.POST or None)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    UID = None
    WID = 0
    order_list=[]
    if request.user.is_authenticated:
        current_user = request.user
        UID = current_user.id
    if form.is_valid():
        instance = form.save(commit=False)
        wh = Warehouse.objects.all()
        w1 = Warehouse.objects.get(whid = 0)
        len_max =((w1.x - instance.desx)**2 +(w1.y - instance.desy)**2)**0.5
        for w in wh:
            len_temp = ((w.x - instance.desx)**2 +(w.y - instance.desy)**2)**0.5
            if len_temp < len_max:
                len_max = len_temp
                WID = w.whid
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for c in cart_items:
            a = Aorder.objects.create( 
                    description=c.good.description,
                    amount=c.amount,
                    ups=instance.ups,
                    whid=WID,
                    desx=instance.desx,
                    desy=instance.desy,
                    ID=c.good.ID,
                    userid=UID,
                    email=instance.email,
                    )
            a.save()
            order_list.append(a)
            good = get_object_or_404(Good, ID=c.good_id)
            cart_item = CartItem.objects.get(good=good, cart=cart)
            cart_item.delete()
        to_email = [instance.email,]
        subject  = "Order Confirmation from mini Amazon"
        message  = "You order number list is: " + "\n"
        for a in order_list:
            message += "Order number is " + str(a.ordernum) + "\n"
        email(to_email, subject, message)
    return render(request, 'order_success.html', {'order_list':order_list})


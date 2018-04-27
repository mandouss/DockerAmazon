from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category,Good
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from cart.models import Cart

def index(request):
    text_var = 'Mini Amazon'
    return HttpResponse(text_var)

def allGoodCat(request, c_slug=None):
    c_page = None
    goods_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        goods_list  = Good.objects.filter(category=c_page, available=True)
    else:
        goods_list = Good.objects.all().filter(available=True)
    paginator = Paginator(goods_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        goods = paginator.page(page)
    except(EmptyPage, InvalidPage):
        goods = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category':c_page, 'goods':goods})

def GoodCatDetail(request, c_slug, good_slug):
    try:
        print(c_slug)
        good = Good.objects.get(category__slug=c_slug, slug=good_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/good.html', {'good': good})

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email    = form.cleaned_data.get('email')
            signup_user = User.objects.get(username=username)        
            # customer_group = Group.objects.get(name='Customer')
            # customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:allGoodCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form})

def signoutView(request):
    logout(request)
    return redirect('signin')


    


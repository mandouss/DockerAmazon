from django.shortcuts import render, redirect
from shop.models import Good, Aorder,Category
from django.db.models import Q
from search_app.forms import NewGoodForm, NewCatForm

def searchResult(request):
    goods = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        goods = Good.objects.all().filter(Q(description__contains=query) | Q(detail__contains=query))
    form = NewCatForm()
    return render(request, 'search.html', {'query':query, 'goods':goods,'form':form})

def searchOrder(request):
    aorder = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        try:
            aorder = Aorder.objects.all().filter(Q(ordernum__exact=query))
        except:
            pass
    return render(request, 'search_order.html', {'query':query, 'aorder':aorder})


def createNewCat(request):
    form = NewCatForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        e = Category.objects.all().filter(name__contains=instance.name)
        if e:
            return render(request, 'search.html')
        instance.save()
    form = NewGoodForm()
    return render(request, 'create_new_good.html', {'form': form})

def createNewGood(request):
    form = NewGoodForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        e = Good.objects.all().filter(description__contains=instance.description)
        if e:
            return render(request, 'search.html')
        instance.save()
    return redirect('shop:allGoodCat')


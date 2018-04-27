from django.db import models
from django.urls import reverse
from django.forms import ModelForm
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=119, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True, default='category/classify.png')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shop:goods_by_category', args=[self.slug])

class Good(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=120, unique=True) #good name
    slug = models.SlugField(max_length=120, unique=True)
    detail = models.TextField(blank=True)  #description
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True, default='product/Amazon-icon.png')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'good'
        verbose_name_plural = 'goods'

    def __str__(self):
        return '{}'.format(self.description)
    
    def get_url(self):
        return reverse('shop:GoodCatDetail', args=[self.category.slug, self.slug]) 

class Stock(models.Model):
    gid = models.IntegerField()
    whid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(default=0)

class Aorder(models.Model):
    ordernum    = models.AutoField(primary_key=True)
    userid      = models.IntegerField(blank=True, null=True)
    ID          = models.IntegerField() 
    description = models.CharField(max_length=120)
    amount      = models.IntegerField()
    ups         = models.CharField(max_length=120, blank=True, null=True) #ups account id
    whid        = models.IntegerField(blank=True, null=True)
    desx        = models.IntegerField(default=0)
    desy        = models.IntegerField(default=0)
    goodid      = models.IntegerField(blank=True, null=True)
    truckid     = models.IntegerField(blank=True, null=True)
    truck_ready = models.BooleanField(default=False)
    pack_ready  = models.BooleanField(default=False)
    load_ready  = models.BooleanField(default=False)
    delivered   = models.BooleanField(default=False)
    email       = models.EmailField(default=None)

class Uorder(models.Model):
    ordernum    = models.IntegerField(primary_key=True)
    ID          = models.IntegerField()
    description = models.CharField(max_length=120)
    amount      = models.IntegerField()
    ups         = models.CharField(max_length=120)
    whid        = models.IntegerField()
    desx        = models.IntegerField()
    desy        = models.IntegerField()

class Warehouse(models.Model):
    whid        = models.IntegerField()
    x           = models.IntegerField()
    y           = models.IntegerField()

 

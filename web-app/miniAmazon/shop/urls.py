
from django.urls import path
from . import views

app_name='shop'

urlpatterns =[
        path('', views.allGoodCat, name='allGoodCat'),
        path('<slug:c_slug>/', views.allGoodCat, name='goods_by_category'),
        path('<slug:c_slug>/<slug:good_slug>/', views.GoodCatDetail, name = 'GoodCatDetail'),
  ]

from django.urls import path
from . import views

app_name='search_app'

urlpatterns =[
        path('', views.searchResult, name='searchResult'),
        path('createNewCat/', views.createNewCat, name='createNewGat'),
        path('searchOrder/', views.searchOrder, name='searchOrder'),
        path('createNewCat/createNewGood/', views.createNewGood, name='createNewGood'),
        ]

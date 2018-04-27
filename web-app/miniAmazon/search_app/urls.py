from django.urls import path
from . import views

app_name='search_app'

urlpatterns =[
        path('', views.searchResult, name='searchResult'),
        path('createNewGood/', views.createNewGood, name='createNewGood'),
        path('searchOrder/', views.searchOrder, name='searchOrder'),
        ]

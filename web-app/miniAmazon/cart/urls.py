from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
        path('add/<int:good_id>/', views.add_cart, name='add_cart'),
        path('', views.cart_detail, name="cart_detail"),
        path('remove/<int:good_id>/', views.cart_remove, name="cart_remove"),
        path('full_remove/<int:good_id>/', views.full_remove, name="full_remove"),
        path('order/', views.create_order, name="create_order"),
        path('order/accept_order/', views.accept_order, name="accept_order"),
        ]

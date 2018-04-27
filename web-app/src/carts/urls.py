from django.conf.urls import url

from carts.views import (view_cart, add_cart, cleanCart)

urlpatterns = [
    # url(r'^$', cart_home, name='home'),
    # url(r'update/$',cart_update, name='update'),
    url(r'^view_cart/$', view_cart, name='view_cart'),
    url(r'^add_cart/$', add_cart, name='add_cart'),
    url(r'^clean_cart/$', cleanCart, name='clean_cart'),
]

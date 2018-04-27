from django.conf.urls import url

from goods.views import (
        GoodListView, 
        #good_list_view, 
        #GoodDetailView, 
        #good_detail_view,
        GoodDetailSlugView
        )

urlpatterns = [
    url(r'^$', GoodListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', GoodDetailSlugView.as_view(), name='detail'),
]

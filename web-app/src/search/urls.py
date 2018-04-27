from django.conf.urls import url

from .views import (
        SearchGoodView, 
        )

urlpatterns = [
    url(r'^$', SearchGoodView.as_view(), name='query'),
]

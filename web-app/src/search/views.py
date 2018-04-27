from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from goods.models import Good 
# Create your views here.
class SearchGoodView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchGoodView, self).get_context_data(*args, **kwargs)
        query= self.request.GET.get('q')
        context['query'] = query
        #SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET 
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            lookups = Q(description__icontains=query)
            return Good.objects.search(query)
        return Good.objects.none()
    

        

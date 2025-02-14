from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Store, Staff

class StoreList(generic.ListView):
    model = Store
    ordering ='name'

class StaffList(generic.ListView):
    model = Staff
    ordering = 'name'

    def get_context_data(self,**kwargs):
        context = super().ge_context_data(**kwargs)
        context['store'] = self.store
        return context
    
    def get_queryset(self):
        store = self.store = get_object_or_404(Store, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(store=store)
        return queryset
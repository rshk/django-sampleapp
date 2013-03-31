# Create your views here.
from django.core.urlresolvers import reverse

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import MyObject

class ListObjView(ListView):
    model = MyObject

class CreateObjView(CreateView):
    model = MyObject

class DetailObjView(DetailView):
    model = MyObject

class UpdateObjView(UpdateView):
    model = MyObject

class DeleteObjView(DeleteView):
    model = MyObject

    def get_success_url(self):
        return reverse('sample:list')

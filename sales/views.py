from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
# Create your views here.


def home_view(request):
    hello = 'hello world form the view'
    return render(request, 'sales/home.html', {'hello':hello})


class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
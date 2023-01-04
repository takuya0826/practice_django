from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import *

class Home_view(ListView):
    template_name = 'home.html'
    dir_mst_model = dir_mst
    model = dir_mst_model
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     return super().get_context_data(**kwargs) 

class Dir_detailview(DetailView):
    template_name = 'detail.html'
    dir_mst_model = dir_mst
    model = dir_mst_model
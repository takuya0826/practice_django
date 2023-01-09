from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import *

class Home_view(ListView):
    template_name = 'home.html'
    dir_mst_model = dir_mst
    model = dir_mst_model
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["ACS_R_US"] = access_mst_user.objects.filter(authority='R').select_related('user_mst_id').values("user_mst_id__user_name")
        context["ACS_W_US"] = access_mst_user.objects.filter(authority='W').select_related('user_mst_id').values("user_mst_id__user_name")
        return context

class Dir_detailview(DetailView):
    template_name = 'detail.html'
    dir_mst_model = dir_mst
    model = dir_mst_model
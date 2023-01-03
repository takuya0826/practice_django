from django.urls import path
from .views import Home_view,Dir_detailview

urlpatterns = [
    path('home/', Home_view.as_view(),name='home'),
    path('detail/<pk>',Dir_detailview.as_view(),name='dirdetail')
]

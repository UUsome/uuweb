from django.urls import path 
from . import views



urlpatterns = [
    path('xx', views.TmpcardView.as_view(), name='xx'), # add
]


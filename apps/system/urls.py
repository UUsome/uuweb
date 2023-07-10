from django.urls import path
from .views_user import IndexView, LoginView, LogoutView


# app_name="system"
urlpatterns = [
    # path('', views.testindex, name='testindex'),
    path('dailyreport', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

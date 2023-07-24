from blog import views
from django.urls import path

urlpatterns = [
    path('blogs', views.blog_list, name='blogs'),
    path('blogtag/<str:name>/', views.tag, name='blogtag'),
    path('blogcategory/<str:name>/', views.category, name='blogcategory'),
    path('blogdetail/<int:pk>/', views.detail, name='blogdetail'),
    path('blogarchive/', views.archive, name='blogarchive'),


]

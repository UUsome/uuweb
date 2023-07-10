from django.urls import path
from . import views

# app_name="dailyreport"
urlpatterns = [
    # path('',  x, name=' x'),
    path('myreport', views.MyReportView.as_view(), name='myreport'),
    path('myreport/create', views.ReportCreateView.as_view(), name='myreport-create'),
    path('myreport/detail', views.ReportDetailView.as_view(), name='myreport-detail'),


]



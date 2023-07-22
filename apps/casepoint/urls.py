from django.urls import path
from . import views

# app_name="testuu"
urlpatterns = [
    path('', views.myindex, name='myindex'),
    path('caseadd', views.CaseAddView.as_view(), name='caseadd'),
    path('caselist', views.CaseListView.as_view(), name='caselist'),
    path('casedetail/<int:Case_title_id>', views.CaseDetailView.as_view(), name='casedetail'),
    path('solutiondetail/<int:Case_title_id>/<uuid:uniqueid>/', views.SolutionDetailView.as_view(), name='solutiondetail'),

]

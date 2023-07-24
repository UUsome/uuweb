from plan import views
from django.urls import path

urlpatterns = [

#    path('calendar/', views.calendar, name='calendar'),
#    path('add_event/', views.add_event, name='add_event'),
#    path('update/', views.update, name='update'),
#    path('remove/', views.remove, name='remove'),
#    path('all_events/', views.all_events, name='all_events'),

    path('planschedule', views.PlanScheduleView.as_view(), name='planschedule') ,
    path('planadd', views.AddPlanView.as_view(), name='planadd') ,

    
]



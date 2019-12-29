from django.urls import path
from . import views

# app_name="testuu"
urlpatterns = [
    # path('', views.testindex, name='testindex'),
    path('TypeAdd', views.TypeAdd.as_view() , name='TypeAdd'),
    path('typeList', views.typeList, name='typeList'),
    path('FrameAdd', views.FrameAdd.as_view(), name='FrameAdd'),
    path('', views.frameList, name='frameList'),
    path('SolutionAdd/<int:type_id>/<int:frame_union>', views.SolutionAdd.as_view(), name='SolutionAdd'),
    path('framedetail/<int:type_id>/<int:frame_union>', views.framedetail, name='framedetail'),
    path('solutiontail/<int:type_id>/<int:frame_union>/<int:solution_union>', views.solutiontail, name='solutiontail'),

]

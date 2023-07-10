from django.contrib import admin
from .models import TypeDetail,Frame,Solution


@admin.register(TypeDetail)
class TypeDetailAdmin(admin.ModelAdmin):
    list_display = ('p_type_id','level','name','is_show','add_time', 'remark',)


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('type','frame_union','title_content','name','creater','is_show','add_time','remark' )

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('range_flage','frame','name','solution_union','creater','is_show','add_time','remark')


 
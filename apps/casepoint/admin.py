from django.contrib import admin
from . import models

# Register your models here.

class Case_titleAdmin(admin.ModelAdmin):
    list_filter = ["casetitle", "category"]
class Case_contentAdmin(admin.ModelAdmin):
    list_filter = ["casetitle", "casecontent", "sub_title"]
class SolutionAdmin(admin.ModelAdmin):
    list_filter = ["solution", "case_id", "uniqueid", "sys_show"]



admin.site.register(models.Case_title, Case_titleAdmin)
admin.site.register(models.Case_content)
admin.site.register(models.Solution, SolutionAdmin)

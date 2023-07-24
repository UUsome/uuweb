from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.DailySchedule)
class DailyScheduleAdmin(admin.ModelAdmin):
    pass
    
@admin.register(models.PlanSchedule)
class PlanScheduleAdmin(admin.ModelAdmin):
    pass
    
@admin.register(models.FeedbackSum)
class FeedbackSumAdmin(admin.ModelAdmin):
    pass




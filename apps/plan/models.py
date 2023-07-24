from django.db import models

# Create your models here.
class DailySchedule(models.Model):
    cat_choices = (('日程安排', '日程安排'), ('项目记录', '项目记录'), ('备忘mark', '备忘mark'))
    category = models.CharField(max_length=20, choices=cat_choices, default='日程安排')
    groupId = models.CharField(max_length=20,default='')
    title = models.TextField(verbose_name='日程安排')
    user = models.CharField(max_length=12,verbose_name="执行人员",default='')
    start = models.DateTimeField(default='', verbose_name='开始时间')
    end = models.DateTimeField(default='', verbose_name='结束时间')
    sys_add = models.DateField(auto_now=True, verbose_name="添加时间")
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    
    def __str__(self):
        return self.category,self.content

    class Meta:
        verbose_name = '日程安排'
        verbose_name_plural = verbose_name


class PlanSchedule(models.Model):
    PRIORITY_choices = (
    ('高','高'),
    ('中','中'),
    ('低','低'),
    ('回归','回归')
    )
    task_id = models.CharField(max_length=255,verbose_name="任务名称",default="")
    p_start_time = models.DateField(auto_now=False, blank=True, null=True, verbose_name="计划开始时间",default="")
    p_finish_time = models.DateField(auto_now=False, blank=True, null=True, verbose_name="计划结束时间",default="")
    a_start_time = models.DateField(auto_now=False, blank=True, null=True, verbose_name="实际开始时间",default="")
    a_finish_time = models.DateField(auto_now=False, blank=True, null=True, verbose_name="实际结束时间",default="")
    progress = models.CharField(max_length=4,verbose_name="完成进度",default="")
    priority = models.CharField(max_length=6,blank=True,null=True,choices=PRIORITY_choices,verbose_name="优先级",default="中")
    executor = models.CharField(max_length=12,verbose_name="执行人员",default="未分配")
    plan_prev = models.IntegerField(default=1,verbose_name='任务上级')
    plan_next = models.IntegerField(default=1,verbose_name='任务上级')
    remark = models.TextField(blank=True,null=True, verbose_name="备注",default="")
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    def __str__(self):
        return self.task_id

    class Meta:
        db_table = "test_progress_schedule"
        ordering = ['p_start_time']
        verbose_name = '计划进度'
        unique_together = ('task_id','plan_prev','plan_next')
        
        
# Create your models here.
class FeedbackSum(models.Model):
    part_choices = (('计划进度', '计划进度'), ('日程安排', '日程安排'))
    part_name = models.CharField(max_length=8,blank=True,null=True,choices=part_choices,verbose_name="优先级",default="中")
    part_id = models.IntegerField(default='',verbose_name='计划表ID')
    content = models.TextField(verbose_name='反馈')
    sys_add = models.DateField(auto_now_add=True, verbose_name="添加时间")
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '反馈总结'
        verbose_name_plural = verbose_name
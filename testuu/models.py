from django.db import models

# Create your models here.

# 类型表设计 TypeDetail (id,P_type,name,add_time,is_show,remark)
class TypeDetail(models.Model):
    p_type_id = models.IntegerField(default='0',verbose_name='父级type')
    level = models.IntegerField(default=0,verbose_name='级别')
    name = models.CharField(max_length=64,verbose_name='框架分类')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')

    # 定义表的属性信息
    class Meta:
        ordering = ["id"]

    # 定义静态方法
    def  __str__(self):
        return self.p_type_id,self.level, self.name


# 2，框架表设计 frame (id,type_id,order_flage,name,creater,add_time,is_show,remark)
class Frame(models.Model):
    type = models.ForeignKey(TypeDetail, on_delete=models.CASCADE, null=False, verbose_name='类型')
    frame_union = models.IntegerField(default='0',verbose_name='frame唯一号')
    title_content = models.IntegerField(default='0',verbose_name='标题内容标识0：标题，1：内容')
    name = models.CharField(max_length=64,verbose_name='框架')
    # creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')
    # 定义静态方法
    def  __str__(self):
        return self.name

# 3，方案表设计 solution (s_order[第几个方案],frame_id,name,creater,add_time,is_show,remark)
class Solution(models.Model):
    range_flage = models.IntegerField(default='0',verbose_name='属于第几个方案')
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, null=False, verbose_name='类型')
    name = models.CharField(max_length=64,verbose_name='框架')
    solution_union = models.IntegerField(default='0',verbose_name='solution唯一号')
    # creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    is_show = models.IntegerField(default=1,verbose_name='删除字段')
    add_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    remark = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'备注')
    # 定义静态方法
    def  __str__(self):
        return self.name


from django.db import models


# Create your models here.

# 2，框架表设计 frame (id,type_id,order_flage,name,creater,add_time,is_show,remark)
class Case_title(models.Model):
    category_choices = (('学习工具', '学习工具'), ('思考工具', '思考工具'), ('分类工具', '分类工具'), ('分步工具', '分步工具'))
    category = models.CharField(max_length=20, choices=category_choices, default='0', verbose_name="类型")
    casetitle = models.CharField(max_length=64,verbose_name='框架标题')
    caseprofile = models.CharField(max_length=200,null=True, blank=True,verbose_name='简介')
    # creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    sys_add = models.DateTimeField(auto_now=True,verbose_name="创建时间")

    # 定义静态方法 (用处之一：在admin显示)

    def __str__(self):
        return self.id,self.category,self.casetitle,self.sys_show

class Case_content(models.Model):
    casecontent = models.CharField(max_length=200,verbose_name='框架内容')
    casetitle = models.ForeignKey(Case_title, on_delete=models.CASCADE, null=False, verbose_name='标题')
    sub_title = models.IntegerField(default='0', verbose_name='0，有输入；1，子标题没有输入')
    # creater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name='用户')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    sys_add = models.DateTimeField(auto_now=True,verbose_name="创建时间")

    # 定义表的属性信息
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.casetitle,self.casecontent,self.sub_title,self.sys_show


# 3，方案表设计 solution (Uniqueid,frame_id,name,creater,add_time,is_show,remark)
class Solution(models.Model):
    case_id =  models.IntegerField(default='0',verbose_name='Case_content_id')
    uniqueid =  models.CharField(max_length=60,verbose_name='方案唯一标识')
    solution = models.CharField(max_length=200,verbose_name='方案')
    is_title = models.IntegerField(default='1', verbose_name='1,标题；0，内容')
    creater = models.CharField(max_length=64,verbose_name='创建人')
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    sys_add = models.DateTimeField(auto_now=True,verbose_name="创建时间")

    # 定义静态方法
    def __str__(self):
        return self.case_id,self.solution,self.uniqueid,self.is_title,self.sys_show


from django.db import models

# Create your models here.
class Tmpcard(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField()
    sys_show = models.IntegerField(default=1,verbose_name='删除字段')
    sys_add = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    def __str__(self):
        return self.body
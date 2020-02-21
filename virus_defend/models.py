from __future__ import unicode_literals
from django.db import models


choice = (
    (1,'良好'),
    (2,'不佳'),
    (3,'确诊'),
)
class Healthstate(models.Model):
    temp = models.CharField(max_length= 30,verbose_name='体温')
    state = models.IntegerField (choices=choice,default= '良好',verbose_name='身体健康状态')
    pub_time = models.DateTimeField(auto_now=True,verbose_name='时间')
    place = models.CharField(max_length= 60,verbose_name='所在地区')

    def __str__(self):
        return self.place
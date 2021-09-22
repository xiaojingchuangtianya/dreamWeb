from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Auth(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="用户名")#连接关联到数据库用户
    qqOpenId=models.CharField(max_length=64,verbose_name="QQ的唯一标识符号",db_index=True)
    createTime=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updateTime=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        verbose_name="qq账号关联"
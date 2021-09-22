from django.db import models
# Create your models here.


class ImgType(models.Model):
    typeName=models.CharField(max_length=50,verbose_name="类别")

    def __str__(self):
        return self.typeName
#url为主键，唯一路径，
#imgType可不指定，不指定我默认缺省为ramdon
#热度不指定的自动为0
class Picture(models.Model):
    url=models.CharField(max_length=50,verbose_name="文件路径",primary_key=True)
    imgType=models.ForeignKey(to=ImgType,null=True,default=1,on_delete=models.DO_NOTHING)
    imgSize=models.CharField(max_length=30,verbose_name="图片尺寸",default="1980*1080")
    hot=models.IntegerField(verbose_name="图片观看热度",default=0)
    download=models.IntegerField(verbose_name="被下载次数",default=0)
    def __str__(self):
        return self.url



from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class BlogType(models.Model):
    typeName=models.CharField(max_length=50,verbose_name="类别", unique=True)
    def __str__(self):
        return self.typeName
    class Meta:
        ordering=("-id",)

class Hot(models.Model):
    hotRate=models.IntegerField(verbose_name="热度",default=0)
    def __str__(self):
        return str(self.hotRate)
    class Meta:
        ordering=("hotRate",)

class Blog(models.Model):
    title=models.CharField(max_length=50,verbose_name="博客标题")
    hot=models.ForeignKey(Hot,on_delete=models.DO_NOTHING,verbose_name="热度")
    type=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,verbose_name="博客分类")
    content=RichTextUploadingField(verbose_name="博客内容")
    createTime=models.DateTimeField(auto_now=True,auto_created=True,verbose_name="创作时间")
    author=models.ForeignKey(User,models.CASCADE)
    class Meta:
        ordering=("-hot",)
    def __str__(self):
        return self.title

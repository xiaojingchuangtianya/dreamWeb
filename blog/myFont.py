from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Blog

class MyForms(forms.ModelForm):
    content=forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':"ckContentInput"}),required=True)
    title=forms.CharField(max_length=50,
                          min_length=6,
                          required=True,
                          error_messages={
                              "required":"标题为必填项，请填写标题！",
                              "min_length":"长度不要少于6个字符",
                              "max_length":"长度不要超过50个字符"},
                          widget=forms.TextInput({"placeholder":"请输入标题","autocomplete":"off"})
                          )
    class Meta:
        model=Blog
        fields =("title","content","type")



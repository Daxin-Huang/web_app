from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model): # 这个模型的标题功能
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model): # 这个模型的条目功能
    """用户所学习的关于某个主题的具体知识条目"""
    topic = models.ForeignKey(Topic, on_delete=None)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'


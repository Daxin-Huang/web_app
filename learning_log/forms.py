from django import forms

from .models import Topic, Entry

# 我的理解，把模型中的类和表单联系到一起，这个表单的提交就用于建立这个类的实例对象
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


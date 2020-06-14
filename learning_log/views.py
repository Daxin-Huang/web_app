from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    return render(request, 'learning_log/index.html')    

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)

def topic(request, topic_id): # 特定的topic
    topic = Topic.objects.get(id=topic_id)
    # 通过外键来读取entry这一属性
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)

def new_topic(request):
    """添加新主题"""
    # 未提交数据： 创建一个新表单
    if request.method != 'POST':
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            # 这里是直接保存，因为
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topics'))
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)

def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求， 使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据， 对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topic',
                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)


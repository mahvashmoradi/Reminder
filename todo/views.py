from datetime import datetime

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from .models import Task, Categories


class TaskView(ListView):
    model = Task
    # queryset = Task.objects.all()
    template_name = 'todo/Task_list.html'
    # queryset = model.objects.filter(due_date__lt=timezone.now())
    # queryset = model.due_manager.expired()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of expired task and live task
        context['expired_task'] = Task.due_manager.expired()
        context['live_task'] = Task.due_manager.live()
        return context

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return str(obj)
        return super().default(obj)


class JSONTaskListView(View):
    def get(self, request, *args, **kwargs):
        qs = Task.due_manager.all()
        data = serialize("json",list( qs), cls=LazyEncoder)
        return HttpResponse(data)

    # def get(self, request, *args, **kwargs):
    #     qs=serializers.serialize("json", list(Task.due_manager.all()),ensure_ascii=False)
    #     return HttpResponse(qs)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/Task_details.html'


class CategoriesView(ListView):
    model = Categories
    template_name = 'todo/Categories_list.html'
    # queryset = Categories.objects.annotate(c=Count('categories_item')).filter(c__gt=0)
    # queryset = Categories.categories_manager.empty()

    # def get_queryset(self):
    #     queryset = {'null_categories': Categories.objects.annotate(c=Count('categories_item')).filter(c=0),
    #                 'notnull_categories': Categories.objects.annotate(c=Count('categories_item')).filter(c__gt=0)}
    #
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of empty category and full category
    #     context['empty_categories'] = Categories.objects.annotate(c=Count('categories_item')).filter(c=0)
    #     context['full_categories'] = Categories.objects.annotate(c=Count('categories_item')).filter(c__gt=0)
    #     return context

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of empty category and full category
        context['empty_categories'] = Categories.categories_manager.empty()
        context['full_categories'] = Categories.categories_manager.full()
        return context


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'todo/Categories_detail.html'

    def get_object(self):
        course = get_object_or_404(Categories, pk=self.kwargs['pk'])
        return course.categories_item.all()


class AddTaskView(CreateView):
    # form_class = TaskForm
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')
    template_name = 'todo/Task_add.html'


class AddCategoryView(CreateView):
    # form_class = CategoryForm
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('categories_list')
    template_name = 'todo/category_add.html'


class TaskEditView(UpdateView):
    model = Task
    # fields = ('title', 'description',)
    fields = '__all__'
    template_name = 'todo/task_edit.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):  # new
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoriesEditView(UpdateView):
    model = Categories
    # fields = ('title', 'body',)
    fields = '__all__'
    template_name = 'todo/categories_edit.html'
    success_url = reverse_lazy('categories_list')


class CategoriesDeleteView(DeleteView):  # new
    model = Categories
    template_name = 'todo/categories_delete.html'
    success_url = reverse_lazy('categories_list')

from django.urls import path
from .views import TaskView, CategoriesView, TaskDetailView, AddTaskView, \
    CategoriesDetailView, AddCategoryView, TaskEditView, TaskDeleteView,CategoriesEditView,\
    CategoriesDeleteView, JSONTaskListView

urlpatterns = [
    path('', TaskView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/edit-task/', TaskEditView.as_view(), name='task_edit'),
    path('<int:pk>/deletetask/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/delete_categories/', CategoriesDeleteView.as_view(), name='categories_delete'),
    path('<int:pk>/edit_categories/', CategoriesEditView.as_view(), name='categories_edit'),
    path('Categories/', CategoriesView.as_view(), name='categories_list'),
    path('<int:pk>/Categories/', CategoriesDetailView.as_view(), name='categories_item'),
    path('addtask/', AddTaskView.as_view(), name='add_task'),
    path('addcategoty/', AddCategoryView.as_view(), name='add_category'),
    path('download-tasks/', JSONTaskListView.as_view(), name='download-tasks'),
]

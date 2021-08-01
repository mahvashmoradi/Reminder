from django.db import models
# Create your models here.
from django.urls import reverse
from .manager import CategoriesManager, DueManager


class Categories(models.Model):
    # name
    name = models.CharField(max_length=50)
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)
    # categories_date manager
    categories_manager = CategoriesManager()
    # # slug
    # slug= models.SlugField()

    def get_absolute_url(self):
        return reverse('task_edit', args=[str(self.id)])

    def __str__(self):
        return self.name


class Task(models.Model):
    ENABLE = "enable"
    DISABLE = 'disable'
    DOING = 'doing'
    DONE = 'done'
    EXPIRE = 'expire'
    ARCHIVE = 'archive'
    UNKNOWN = 'unknown'
    STATUS_TASK = [
        (DISABLE, 'غیرفعال'),
        (ENABLE, 'فعال'),
        (DOING, 'در حال انجام'),
        (DONE, 'انجام شده'),
        (EXPIRE, 'منقضی'),
        (ARCHIVE, 'ارشیو'),
        (UNKNOWN, 'بی سرپرست'),
    ]

    PRIORITY_TASK = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),
    ]

    class Meta:
        ordering = ('due_date',)
        # verbose_name = 'تسک'
        # verbose_name_plural = 'تسک ها'

    # # user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=250)
    # description
    description = models.TextField()
    # priority 1
    priority = models.IntegerField(choices=PRIORITY_TASK, default=4)
    # status
    status = models.CharField(max_length=10, choices=STATUS_TASK, default=ENABLE)
    # expire_date
    due_date = models.DateTimeField()
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)
    # categories
    categories = models.ManyToManyField(Categories, related_name='categories_item')
    # due_date manager
    due_manager = DueManager()

    def get_absolute_url(self):
        return reverse('categories_edit', args=[str(self.id)])

    def __str__(self):
        return self.title
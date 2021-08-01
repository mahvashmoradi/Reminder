from django.db import models
from django.utils import timezone
from django.db.models import Count


class CategoriesManager(models.Manager):
    def empty(self):
        return self.annotate(c=Count('categories_item')).filter(c=0)

    def full(self):
        return self.annotate(c=Count('categories_item')).filter(c__gt=0)


# class DueQuerySet(models.QuerySet):
#     def expired(self):
#         return self.filter(due_date__lt=timezone.now())


class DueManager(models.Manager):
    # def get_queryset(self):
        # return DueQuerySet(self.model, using=self._db)
    def expired(self):
        return self.filter(due_date__lt=timezone.now())

    def live(self):
        return self.filter(due_date__gte=timezone.now())



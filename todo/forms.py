from django import forms
from .models import Task, Categories

# data= 2021-07-27 18:44:55
class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        # fields = ['title','description','priority']
        fields = '__all__'
        # exclude = ['complete', 'date_of_creation', ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's on your mind today?, "}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your task ..", 'cols': 80, 'rows': 3}),
            # 'expire_date': forms.DateTimeInput(attrs={'cols': 80, 'rows': 3})
# class= vDateField
        }

    # def clean_title(self):
    #     super(TaskForm, self).clean()
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 5:
    #         self._errors['title'] = self.error_class([
    #             'اینم فارسی که خیالت راحت شه'])


# data= 2021-07-27 18:44:55
class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Categories
        # fields = ['title','description','priority']
        fields = '__all__'
        # exclude = ['complete', 'date_of_creation', ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's on your mind today?, "}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your task ..", 'cols': 80, 'rows': 3}),
            # 'expire_date': forms.DateTimeInput(attrs={'cols': 80, 'rows': 3})
# class= vDateField
        }

    # def clean_title(self):
    #     super(TaskForm, self).clean()
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 5:
    #         self._errors['title'] = self.error_class([
    #             'اینم فارسی که خیالت راحت شه'])

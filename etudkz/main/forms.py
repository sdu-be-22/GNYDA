from django import forms
from .models import *
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['coursename', 'teacher', 'icon', 'price']

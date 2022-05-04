# <<<<<<< HEAD
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

# Create your models here.


class Teacher(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
# =======
# >>>>>>> 8405947f5850499c4ec15157c8510f21c27a7a30

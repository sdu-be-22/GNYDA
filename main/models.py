from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# Create your models here.

class Course(models.Model):
    # id = i++
    coursename = models.CharField(max_length=256, null=False)
    teacher = models.CharField(max_length=32, null=False)
    # icon = models.ImageField(upload_to='images' , null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    added = models.ManyToManyField(User, default=None)
    liked = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.coursename}, Teacher: {self.teacher}, price: {self.price}  , {self.added.all()}'


class Test(models.Model):
    coursename = models.CharField(max_length=256, null=False)
    teacher = models.CharField(max_length=32, null=False)
    icon = models.ImageField(upload_to='images' )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.coursename}, Teacher: {self.teacher}, price: {self.price} {self.id}'

class Friends(models.Model):
    # a = models.ForeignKey(User, on_delete=models.CASCADE)
    # friends = models.ManyToManyField(User)
    a = models.CharField(max_length=120)

class Comment(models.Model):
   author = models.CharField(max_length=64)
   course_id = models.IntegerField(null=False)
   post = models.CharField(max_length=64)
   text = models.TextField(max_length=1024)
   date = models.DateTimeField(auto_now_add=True)
   anonymous = models.BooleanField(default=False)
   liked = models.ManyToManyField(User)
   dis = models.ManyToManyField(User , related_name='dislike')
   # child = models.
   # parent = models.OneToOneField('self' , on_delete=models.CASCADE , null=True)
   def __str__(self):
       return f'{self.pk} , {self.course_id}'


class Learning(models.Model):
    user = models.CharField(max_length=64)
    course_id = models.IntegerField(null=False)

    def __str__(self):
        return f' user: {self.user}, course_id: {self.course_id} {self.id}'

# from urllib import request
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import re
from django.shortcuts import render,HttpResponseRedirect , HttpResponse,redirect
from django.utils.datastructures import MultiValueDictKeyError
from main.models import Course
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django. import response
from django.template import response
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import auth,User
from teach.forms import SignUpForm
from main.models import Course
from django.views import generic




def account(request):

    if request.user.is_authenticated:
        return render(request, 'teach/account.html',{
            'username':request.user.username
        })
    else:
        return render(request, 'teach/login.html')


def user(request, username):
    if User.objects.get(username = username) is not None:
        user = User.objects.get(username = username)
        active = request.user

        return render(request, 'teach/user.html',{
                        'user':user,
            }
        )

def liked(request):
    courses = Course.objects.filter(

    )
    return render(request , 'teach/liked1.html',{
        'courses':courses,
        'request':request,
    })

def login_view(request):
    boo = request.user.is_authenticated
    if request.method == 'POST':
        print(123)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)

            return render(request, 'main/header.html', {
                'request': request
            })

            # return render(request, 'main/card.html', {
            #     'request': request
            # })

            return redirect('/course')
            # return redirect('course')

        else:
            return render(request , 'teach/login.html',{
                'msg':'Incorrect '
            })
            # return HttpResponse(13)
    else:
        return render(request, 'teach/login.html',{
        })

def logout_view(request):
    logout(request)
    
def index(request):
    boo = request.user.is_authenticated
    if boo and request.user.is_superuser:
        print(123)
        crs = Course()

        form = crs.icon
        return render(request , 'teach/addCourse.html',{
            'frm':form
        })
    else :
        return render(request,'main/header.html')

def add(request):
    if request.method == 'POST':
        crs = Course()
        coursename = request.POST['coursename']#Ibek
        teacher = request.POST['teacher']#FizX
        price = request.POST['price']#400
        print('asdklmasndjaks')
        print(9999)
        icon = request.FILES['icon']
        crs.coursename = coursename
        crs.teacher = teacher
        crs.price = price
        print(icon)

        coursename = request.POST['coursename']#Ibek
        teacher = request.POST['teacher']#FizX
        price = request.POST['price']#400
        # if request.FILES['icon'] is None:
        #     return render(request, 'teach/addCourse.html')
        try:
            icon = request.FILES['icon']
        except MultiValueDictKeyError:
            icon = 'course_images/images.png'
        # print(icon)

        # crs.icon = 'course_images/'+icon
        object = Course.objects.create(coursename = coursename,
                                       teacher = teacher,
                                       price = price,
                                       icon = icon)
        object.save()
        # crs.save()
        return render(request , 'teach/addCourse.html',{
            'msg':f"Added to courses {coursename}, {teacher}, {price}"
        })

def change(request , courseid):
    if request.method == 'POST':
        coursename = request.POST['coursename']  # Ibek
        teacher = request.POST['teacher']  # FizX
        price = request.POST['price']  # 400
        try:
            icon = request.FILES['icon']
        except MultiValueDictKeyError:
            icon = 'course_images/images.png'
        # print(icon)

        # crs.icon = 'course_images/'+icon
        object = Course.objects.get(id = courseid)
        object.coursename = coursename
        object.teacher = teacher
        object.price = price
        object.icon = icon
        object.save()
        # crs.save()
        return redirect('/course')


def reglog(request):
    if request.user.is_superuser:
        crs = Course()
        form = crs.icon
        print("sljadajskdks")
        return render(request,'teach/addCourse.html' , {
            'frm': form
            })
    else :
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            user = request.POST['username']
            if User.objects.filter(username=user).exists():
                # print(12312321)
                return render(request, 'teach/signup.html',{
                    'msg':'User already exists plaese choose another username',
                    'form':form,
                })
            elif form.is_valid():
                form.save()
            else:
                return render(request, 'teach/signup.html', {
                    'msg': 'Your password or username entered incorrectly',
                    'form': form,
                })
        form = UserCreationForm()
        return render(request, 'teach/signup.html' , {
            'form':form
        })

def regist(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form = UserCreationForm()

    return render(request, 'teach/regorlog.html' , {
        'form':form
    })


# class UserEditView(request):
    # form_class = UserChangeForm
    # template_name = 'teach/edit_profile.html'
    # success_url = reverse_lazy('account')

    # def get_object(self):
    #     return self.request.user
    # if request.method == 'POST':
    #     print(111)
    # else:
    #     print(123)


    # return render(request , 'teach/edit_profile.html')
    # if request.method == 'POST':
        # form = UserCreationForm(request='POST')
        # if form.is_valid():
        #     form.save()
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # confirm = request.POST['confirm']

        # form = Teacher(request.POST)

        # if form.is_valid():
        #     form.save()
        #
        #
        #     return redirect('login')
        #     return render(request, 'teach/signup.html',{
        #         'msg':'Successful'
            # })
        # else:
        #     form = Teacher()
            # return render(request , 'teach/signup.html',{
            #     'username': username,
            #     'email': email,
            #     'password': password,
            #     'confirm':password==confirm,
            #
            # })
    # else:
    #     return render(request, 'teach/signup.html',{'form':form})
    # else:
    #     return render(request, 'teach/signup.html')
# =======
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm = request.POST['confirm']
#         return render(request , 'teach/signup.html',{
#             'username': username,
#             'password': password,
#             'confirm':password==confirm,
#         })
#
#
#     else:
#         return render(request, 'teach/signup.html')
#

# >>>>>>> 8405947f5850499c4ec15157c8510f21c27a7a30


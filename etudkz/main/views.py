from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import *
from .models import *
# Create your views here.
from django.db.models import Q
from .forms import EmailPostForm
from django.core.mail import send_mail
from django import forms
from .models import *



def course(request):
    courses = Course.objects.all()

    return render(request , 'main/Card.html',{
        'courses':courses,
    })
def course_test(request):
    courses = Course.objects.all()

    return render(request , 'main/card_give.html',{
        'courses':courses,
    })

def header(request):
    boo = request.user.is_authenticated()
    return render(request , 'main/profile.html',{
        'request':request
    })


def delcomment(request , commentId):
    c = Comment.objects.get(pk=commentId)
    c.delete()
    return redirect("/"+str(c.course_id))

def logout_view(request):
    logout(request)
    return redirect('/')


def delete(request , courseid):
    crs = Course.objects.get(id=courseid)
    crs.delete()
    return redirect('course')



def srch(request ):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        m = Course.objects.filter(
            coursename__contains=name
        )
        list = []
        for el in m:
            list.append(el)

        l = Course.objects.filter(
            teacher__contains=name
        )

        for el in l:
            if not list.__contains__(el):
                list.append(el)
        return render(request, 'main/Card.html',{
            'courses':list
        })
    else:
        return render(request, 'main/Card.html',{
            'courses':courses
        });


def addComC(request,courseid , parent):
    if request.method== 'POST':

        cmnt = request.POST['com_child']

        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        if not request.user.is_authenticated:
            return render(request, 'main/About.html', {
                'request':request,
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
                'msg': 'You not logged in'
            })
        else:
            com = Comment()
            com.author = request.user.username
            com.course_id = courseid
            com.post = request.POST['post']
            com.text = cmnt
            com.date = timezone.now()
            anon = request.POST.get('anon', False)
            com.anonymous = anon
            com.save()
            return render(request, 'main/About.html', {
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
            })

        return render(request, 'main/About.html', {
            'name': name,
            'teacher': teacher,
            'id': price,
            'crsid': courseid,
            'comments': comment,
        })
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        return render(request, 'main/About.html', {
            'name': name,
            'teacher': teacher,
            'id': price,
            'comments': comment,
            'crsid': courseid,
            'msg':'nopost'
        })



def addCom(request,courseid):
    if request.method== 'POST':

        cmnt = request.POST['com']
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )

        if not request.user.is_authenticated:
            return render(request, 'main/About.html', {
                'request':request,
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
                'msg': 'You not logged in',
                'c_id': c.id,
            })
        else:
            com = Comment()
            com.author = request.user.username
            com.course_id = courseid
            com.post = request.POST['post']
            com.text = cmnt
            com.date = timezone.now()
            anon = request.POST.get('anon', False)
            com.anonymous = anon
            # com.time = str(timezone.now().time())

            # print(com.time)
            com.save()
            return render(request, 'main/About.html', {
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
                'c_id': c.id,
            })

    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        return render(request, 'main/About.html'
                      , {
            'name': name,
            'teacher': teacher,
            'id': price,
            'comments': comment,
            'crsid': courseid,
            'msg':'nopost',
            'c_id': c.id,
        })

# class prof(request):
    # if request.method ==

def edit(request):
    if request.method == 'POST':
        # reverse('')
        # print(123)
        name = request.POST['firstname']
        last = request.POST['lastname']
        mail = request.POST['email']
        user = request.user
        user.first_name = name
        user.last_name = last
        user.email = mail
        user.save()
        return redirect('/account')
        # print(user.email)
    else:
        return render(request, 'teach/edit_profile.html')
    return render(request, 'teach/edit_profile.html')


def edit_course(request , courseid):
    course = Course.objects.get(id = courseid)
    print(course)
    return render(request, 'main/edit_Course.html',{
                  'course': course,
    })

def openC(request,courseid):
    len = Course.objects.all().last().id


    if(courseid > len or courseid<1):
        return HttpResponse("ERROR")
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        if comment.__len__() == 0:

            return render(request,'main/About.html',{
                'request':request,
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,

            })
        else:
            return redirect('addcmnt',courseid=courseid)

def like(request , courseid):
    crs = Course.objects.get(pk = courseid)
    cont = False
    if crs.added.contains(request.user):
        crs.added.remove(request.user)
        crs.save()
    else:
        crs.added.add(request.user)
        crs.save()



    courses = Course.objects.all()
    # return reverse('course')
    return render(request , 'main/Card.html',{
        'courses':courses,
        'request':request,
    })

def chec_learning(request):
    name = request.user.username
    user_id = User.objects.get(username = name).pk
    learn_courses = Course.objects.filter(
        Q(learn_user = user_id)
    )
    a = len(learn_courses)


    return render(request, 'main/Learning.html', {
        'a':a,
        'name':name,
        'courses': learn_courses,
        'request': request,
    })

def add_to_learning(request, course_id):
    crs = Course.objects.get(pk=course_id)
    if crs.learn_user.contains(request.user):
        msg = 'You have already added this course'
    else:
        crs.learn_user.add(request.user)
        crs.save()
        msg = 'Course added'
    name = crs.coursename
    teacher = crs.teacher
    price = crs.price
    comment = Comment.objects.filter(
        Q(course_id=crs.pk)
    )
    return render(request, 'main/About.html', {
        'name': name,
        'teacher': teacher,
        'id': price,
        'comments': comment,
        'crsid': course_id,
        'msg': msg
    })


def delern(request ,courseid):
    crs = Course.objects.get(pk=courseid)
    crs.learn_user.remove(request.user)
    crs.save()
    return redirect('learn')


def post_share(request, c_id):
    # Retrieve post by id
    course = get_object_or_404(Course, id=c_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                course.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                      f"{course.coursename}"
            message = f"Read {course.coursename} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'tazhibayda@gmail.com',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'main/share.html', {'course': course,
                                                'form': form,
                                                'sent': sent})




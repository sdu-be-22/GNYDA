from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render , HttpResponse,redirect
from django.urls import *
from .models import *
# Create your views here.
from django.db.models import Q

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
    return render(request,'teach/login.html')


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
            # com.time = str(timezone.now().time())

            # print(com.time)
            com.save()
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
    
    learn_courses = Learning.objects.filter(
        Q(user = name)
    )
    course_name = learn_courses.all()

    return render(request, 'main/Learning.html', {
        'name': name,
        'crs':course_name,
        # 'name_course':name_course,
        
    })
def learning_card(request,courseid):
    c = Course.objects.get(pk = courseid)
    name = c.coursename
    price = c.price
    teacher = c.teacher
    return render(request, 'main/Learning.html', {
        'crs_name':name,
        'teacher' : teacher,
        'price' : price,
    })

def add_to_learning(request, course_id):
    learn = Learning()
    learn.user = request.user.username
    learn.course_id = course_id
    if Learning.objects.filter(course_id=course_id).exists():
        return render(request, 'main/About.html', {
            'crsid': course_id,
            'msge':'You have already added this course to learning'
        })
    else:
        learn.save()
        return render(request, 'main/About.html', {
            'crsid': course_id,
            'msge': 'added to the learning'
        })

def delern(request ,courseid):
    learn = Learning.objects.filter(course_id=courseid)
    learn.delete()

    return redirect('learn')


from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('',views.index, name='index'),
    path('test/',views.reglog , name='reglog'),
    path('add', views.add , name = 'add'),
]
urlpatterns += staticfiles_urlpatterns()
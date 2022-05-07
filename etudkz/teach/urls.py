from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from etudkz import settings
from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('',views.index, name='index'),
    path('test/',views.reglog , name='reglog'),
    path('add', views.add , name = 'add'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
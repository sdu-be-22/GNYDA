from django.contrib import admin
from django.urls import path, include

import main
import teach.views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('teach/', include('teach.urls')),
    path('account', teach.views.account, name='account'),
    path('user/<str:username>', teach.views.user , name = 'user'),
    path('account/liked', teach.views.liked, name='liked'),

]



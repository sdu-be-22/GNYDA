from django.contrib import admin
from django.urls import path, include

import main
import teach.views

# from etudkz.main import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('teach/', include('teach.urls')),
    path('account', teach.views.account, name='account'),
    path('user/<str:username>', teach.views.user , name = 'user'),
    path('account/liked', teach.views.liked, name='liked'),
    path('account/edit', main.views.edit, name='edit'),
    path('editcourse/<int:courseid>' , main.views.edit_course , name='edit_course'),
    # path('login/', teach.views.login_view, name='logging'),

]



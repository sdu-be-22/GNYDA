from django.urls import path

import teach.views
from . import views
# from teach import views
urlpatterns = [
    # path('',views.course),
    path('' , views.course , name = 'course'),
    path('<int:courseid>' , views.openC),
    path('del/<int:courseid>' , views.delete  , name='delete'),
    path('result' , views.srch, name='searching'),
    path('logout', views.logout_view , name = 'logout' ),
    path('<int:courseid>/addcmnt', views.addCom , name='addcmnt'),
    path('delcom/<int:commentId>',views.delcomment ,name='delcom'),
    path('account/Learning/', views.chec_learning, name='learn'),
    path('addlearn/<int:course_id>', views.add_to_learning, name='addlearn'),
    path('delern/<int:courseid>', views.delern, name='delern'),
    path('like/<int:courseid>', views.like , name='like' ),
    path('learning_card/<int:courseid>', views.learning_card , name='learning_card' ),
    path('account/edit_profile/', teach.views.UserEditView.as_view(), name='edit_profile')

]
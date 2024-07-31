from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import tasks,taskdtl,taskdel,taskmod,taskadd,login_view

urlpatterns = [
    path('',tasks,name='tasks'),
    path('task/<int:pk>',taskdtl,name='taskdtl'),
    path('taskdel/<int:pk>',taskdel,name='taskdel'),
    path('taskmod/<int:pk>',taskmod,name='taskmod'),
    path('taskadd/',taskadd,name='taskadd'),




    path('accounts/login/',login_view,name='login'),
    path('login/',login_view,name='aclogin'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]

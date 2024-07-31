from django.urls import path,include

from .views import tasks,taskmod,taskadd,taskdel,taskdtl
urlpatterns = [
    path('',tasks,name='tasks'),
    path('task/<int:pk>',taskdtl,name='taskdtl'),
    # path('taskdel/<int:pk>',taskdel,name='taskdel'),
    # path('taskmod/<int:pk>',taskmod,name='taskmod'),
    # path('taskadd/',taskadd,name='taskadd'),
]
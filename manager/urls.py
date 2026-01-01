from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.taskView, name='tasks'),
    path('tasks/create',views.taskCreateView,name='task-create'),
    path('tasks/update/<int:id>',views.taskUpdateView,name='task-update'),
    
]
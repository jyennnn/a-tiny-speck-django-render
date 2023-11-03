from django.urls import path
from base.views import yogalogs_views as views


urlpatterns = [
    path('', views.getYogaLogs, name="allYogaLogs"),
    
    path('logYogaPractice/', views.logYogaPractice, name='logYogaPractice'),
        
    path('<str:pk>/', views.getYogaLogsByUser, name="YogaLogsByUser"),

]
from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/', views.room_name, name='room'),
]
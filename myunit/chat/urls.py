from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/', views.message_list, name='message-detail'),
    path('users/<int:pk>', views.user_list, name='user-detail'),
    path('users/', views.user_list, name='user-list'),
]
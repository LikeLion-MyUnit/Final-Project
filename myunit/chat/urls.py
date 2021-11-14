from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('messages/', views.message_list, name='message-list'),
    path('users/<int:pk>', views.user_list, name='user-detail'),
    path('users/', views.user_list, name='user-list'),
    path("create/", views.MessageCreate.as_view()),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/', views.message_list, name='message-detail'),
]
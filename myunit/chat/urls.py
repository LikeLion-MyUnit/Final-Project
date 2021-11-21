from django.urls import path, include
from . import views

urlpatterns = [
    path('messages/', views.Message_Post, name='message-detail'),
    path('messages/<int:sender>/<int:receiver>',views.Message_Get)
]
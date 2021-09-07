from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('profile/', views.ProfileCreate.as_view()),
    path('secondprofile/', views.SecondProfileCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

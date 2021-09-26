from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 유저 회원가입
    path('user/signup/', views.UserCreate.as_view()),
    # 유저 업데이트. 삭제
    path('user/<int:pk>/', views.UserDetail.as_view()),
    # 유저 프로필 생성
    path('profile/create/', views.ProfileCreate.as_view()),
    # 유저 프로필 업데이트, 삭제
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

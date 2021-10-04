from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # 글쓰기
    path('create/', views.PostCreate.as_view()),
    path('update/<int:pk>/', views.PostDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('post_like_toggle/<int:pk>/',
         views.post_like_toggle),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

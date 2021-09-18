from django.contrib import admin
from .models import Profile, CustomUser, Post, Category

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)

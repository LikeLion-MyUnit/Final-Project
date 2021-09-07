from django.contrib import admin
from .models import Profile, CustomUser, SecondProfile

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(SecondProfile)

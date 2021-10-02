from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Profile, CITY_CHOICES, INTEREST_CHOICES

# Create your models here.

class Category(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject


class Post(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_user")
    title = models.CharField(max_length=50)
    contest = models.CharField(max_length=50)   # 대회명
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 
    category = models.ForeignKey(
        "Category", on_delete=CASCADE, related_name='post')    # 모집/초대
    poster = models.ImageField(blank=False)
    like_count = models.PositiveIntegerField(default=0)  # 좋아요 수
    city = models.CharField(default='선택안함', max_length=80,
                            choices=CITY_CHOICES, null=False)
    interest = models.CharField(
        default='선택안함', max_length=80, choices=INTEREST_CHOICES, null=False)
    # 마감날짜는 나중에 forms에서 DateInput으로 받을 예정
    end_date = models.CharField(max_length=20)
    is_open = models.BooleanField(default=True)  # 마감여부
    recruit = models.PositiveIntegerField(default=0)    # 모집인원
  
    def __str__(self):
        return self.title

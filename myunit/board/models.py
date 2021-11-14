from django.db import models
from django.db.models.deletion import CASCADE

class Post(models.Model):
    id = models.AutoField(primary_key=True)  # post_id
    profile = models.ForeignKey(
        'account.profile', on_delete=models.CASCADE, related_name="profile_user")
    title = models.CharField(max_length=50)
    contest = models.CharField(max_length=50)   # 대회명
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(blank=False)
    like_count = models.PositiveIntegerField(default=0)  # 좋아요 수
    city = models.CharField(default='선택안함', max_length=80, null=False)
    interest = models.CharField(
        default='선택안함', max_length=80, null=False)
    # 마감날짜는 나중에 forms에서 DateInput으로 받을 예정
    end_date = models.CharField(max_length=20)
    is_open = models.BooleanField(default=True)  # 마감여부
    recruit = models.PositiveIntegerField(default=0)    # 모집인원

    def __str__(self):
        return self.title

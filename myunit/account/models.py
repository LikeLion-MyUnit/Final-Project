from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# BaseUserManager : User를 생성하는 Helper 클래스
# AbstractBaseUser : 실제 모델이 상속받아 생성하는 클래스
# PermissionsMixin : 기본 그룹, 허가권 관리 기능 재사용


class UserManager(BaseUserManager):
    use_in_migrations = True

    # 일반 User 생성
    def create_user(self, email, nickname, password):
        if not email:
            raise ValueError('이메일은 필수입니다!')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password,
        )

        user.is_admin = False
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    id = models.AutoField(primary_key=True)

    email = models.EmailField(
        max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(
        max_length=100, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # 사용자의 username field는 email으로 설정
    REQUIRED_FIELDS = ['nickname']  # 필수로 작성해야 하는 field목록

    def __str__(self):
        return self.nickname

CITY_CHOICES = {
        ('seoul', '서울'),  # 오른쪽에 있는 것이 화면에 보임
        ('busan', '부산'),
        ('incheon', '인천'),
        ('daegu', '대구'),
        ('ulsan', '울산'),
        ('gwangju', '광주'),
        ('daejeon', '대전'),
        ('sejong', '세종'),
        ('gangwon', '강원'),
        ('gyeonggi', '경기'),
        ('chungcheong', '충청'),
        ('gyeongsang', '경상'),
        ('jeonra', '전라'),
        ('jeju', '제주'),
        ('none', '선택안함')
    }

INTEREST_CHOICES = {
        ('idea', '기획/아이디어'),
        ('marketing', '광고/마케팅'),
        ('photo', '사진/영상'),
        ('design', '디자인'),
        ('science', '과학/공학'),
        ('business', '창업'),
        ('etc', '기타'),
        ('none', '선택안함')      
    }

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=CASCADE,related_name='profile')

    TIMECNT_CHOICES = {
        ('once', '주 1회'),
        ('twice', '주 2회'),
        ('three', '주 3회'),
        ('four', '주 4회'),
        ('five', '주 5회')
    }

    # character: 팀 활동시 캐릭터/성향/장단점
    # timecnt: 할애할 수 있는 시간
    # mycomment: 팀원들에게 당부하는 말
    # is_open: 프로필 공개 여부

    city = models.CharField(
        default='선택안함', max_length=80, choices=CITY_CHOICES, null=False)
    interest = models.CharField(
        default='선택안함', max_length=80, choices=INTEREST_CHOICES, null=False)
    character = models.CharField(
        default='', max_length=200, null=False, blank=False)   
    timecnt = models.CharField(
        default='', max_length=80, choices=TIMECNT_CHOICES, null=False)
    mycomment = models.CharField(
        default='', max_length=200, null=False, blank=False)
    is_open = models.BooleanField(default=True)    
    
    def __str__(self):
        return str(self.user) 

class Category(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_user")
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=CASCADE, related_name='post')    # 모집/초대
    poster = models.ImageField(blank=False)
    like_count = models.PositiveIntegerField(default=0) # 좋아요 수
    city = models.CharField(default='선택안함', max_length=80, choices=CITY_CHOICES, null=False)
    interest = models.CharField(default='선택안함', max_length=80, choices=INTEREST_CHOICES, null=False)
    end_date = models.CharField(max_length=20)   # 마감날짜는 나중에 forms에서 DateInput으로 받을 예정
    is_open = models.BooleanField(default=True)  # 마감여부
    recruit = models.PositiveIntegerField(default=0)    # 모집인원

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import CASCADE

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


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)

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

    TIMECNT_CHOICES = {
        ('once', '주 1회'),
        ('twice', '주 2회'),
        ('three', '주 3회'),
        ('four', '주 4회'),
        ('five', '주 5회')
    }

    city = models.CharField(
        default='선택안함', max_length=80, choices=CITY_CHOICES, null=False)
    interest = models.CharField(
        default='선택안함', max_length=80, choices=INTEREST_CHOICES, null=False)
    character = models.CharField(       # 팀 활동시 캐릭터/성향/장단점
        default='', max_length=200, null=False, blank=False)
    timecnt = models.CharField(       # 할애할 수 있는 시간
        default='', max_length=80, choices=TIMECNT_CHOICES, null=False)
    mycomment = models.CharField(   # 팀원들에게 당부하는 말
        default='', max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.user) 


class SecondProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)

    portpolio = models.CharField(
        default='', max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.user)

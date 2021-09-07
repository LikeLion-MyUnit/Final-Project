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
        ('busan', '부산'),  # 오른쪽에 있는 것이 화면에 보임
        ('seoul', '서울'),
        ('daegu', '대구'),
        ('none', '선택안함')
    }

    STATUS_CHOICES = {
        ('student', '학생'),
        ('worker', '직장인'),
        ('none', '선택안함')
    }

    city = models.CharField(default='선택안함', max_length=80,
                            choices=CITY_CHOICES, null=False)
    status = models.CharField(
        default='선택안함', max_length=80, choices=STATUS_CHOICES, null=False)
    department = models.CharField(
        default='', max_length=200, null=False, blank=False)
    skill = models.CharField(
        default='', max_length=200, null=False, blank=False)
    interest = models.CharField(
        default='', max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.user)


class SecondProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)

    portpolio = models.CharField(
        default='', max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.user)

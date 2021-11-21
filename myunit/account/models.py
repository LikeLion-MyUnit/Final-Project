from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# BaseUserManager : User를 생성하는 Helper 클래스
# AbstractBaseUser : 실제 모델이 상속받아 생성하는 클래스
# PermissionsMixin : 기본 그룹, 허가권 관리 기능 재사용


class UserManager(BaseUserManager):
    use_in_migrations = True

    # 일반 User 생성
    def create_user(self, email,password,phonenum):
        if not email:
            raise ValueError('이메일은 필수입니다!')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            phonenum=phonenum,
        )

        user.is_admin = False
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
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
    phonenum = PhoneNumberField(default='')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # 사용자의 username field는 email으로 설정

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=CASCADE, related_name='profile')
    user_pk = models.IntegerField(null = True, blank = True)
    nickname = models.CharField(
        max_length=100, null=True, blank=True, unique=True)
    photo = models.ImageField(blank=True, null=True)  # 유저 사진
    gender = models.CharField(
        default='선택안함', max_length=80, null=False)
    city = models.CharField(
        default='선택안함', max_length=80, null=False)
    interest = models.CharField(
        default='선택안함', max_length=80, null=False)
    skill = models.CharField(
        default='', max_length=200, null=False, blank=False)
    mycomment = models.CharField(
        default='', max_length=200, null=False, blank=False)
    portfolio = models.CharField(
        default='', max_length=200, null=False, blank=False)
    is_open = models.BooleanField(default=True)
    # like_posts = models.ManyToManyField(
    #     'board.Post', blank=True, related_name='like_posts ')

    def __str__(self):
        return str(self.user)

# class ProfileImage(models.Model):
#     image = models.ImageField(upload_to='profile_images')
#     user = models.ForeignKey(Profile, on_delete=CASCADE, blank=False)
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
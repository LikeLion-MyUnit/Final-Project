from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# BaseUserManager: User를 생성하는 Helper 클래스
# AbstractBaseUser: 실제 모델이 상속받아 생성하는 클래스

class UserManager(BaseUserManager):
    # 일반 User 생성
    def create_user(self, email, nickname, city, status, department, skill, interest, password=None):
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            password1 = password,
            city = city,
            status = status,
            department = department,  
            skill = skill,
            interest = interest
        )
        user.set_password(password)
        user.save(using=self._db)        
        return user 
    
    # 관리자 User 생성
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            nickname = nickname,
            password1 = password
        )
        user.is_admin = True
        user.save(using=self._db)        
        return user 

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)

    CITY_CHOICES = {
        ('busan','부산'), # 오른쪽에 있는 것이 화면에 보임
        ('seoul', '서울'),
        ('daegu', '대구'),
        ('none', '선택안함')
    }

    STATUS_CHOICES = {
        ('student','학생'),
        ('worker', '직장인'),
        ('none', '선택안함')
    }

    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(max_length=100, null=False, blank=False, unique=True)
    city = models.CharField(default='선택안함', max_length=80, choices=CITY_CHOICES, null=False)
    status = models.CharField(default='선택안함', max_length=80, choices=STATUS_CHOICES, null=False)
    department = models.CharField(default='', max_length=200, null=False, blank=False)
    skill = models.CharField(default='', max_length=200, null=False, blank=False)
    interest = models.CharField(default='', max_length=200, null=False, blank=False) 

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)  

    objects = UserManager()
    
    USERNAME_FIELD = 'email' # 사용자의 username field는 email으로 설정    
    REQUIRED_FIELDS = ['email'] # 필수로 작성해야 하는 field목록
    def __str__(self):
        return self.nickname


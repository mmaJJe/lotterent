from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=20, null = True, blank = True, verbose_name='회원이름')
    phone = models.CharField(max_length=12, null = True, blank = True, verbose_name='전화번호')
    birth = models.CharField(max_length=8, null = True, blank = True, verbose_name='생년월일')
    address = models.CharField(max_length=60, null = True, blank = True, verbose_name='주소')
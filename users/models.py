from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image=models.ImageField(
        "프로필이미지", upload_to = "users/profile", blank=True)
    short_description= models.TextField("소개글",blank=True)
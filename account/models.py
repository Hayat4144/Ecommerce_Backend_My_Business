from email.policy import default
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id   = models.UUIDField(primary_key =True,default=uuid.uuid4,unique=True, editable = False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length =50)
    mobile_no = models.CharField(max_length = 10,unique=True)
    is_superuser  = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now =True,blank =True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','mobile_no']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    


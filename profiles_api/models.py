from django.db import models
from django.contrib.auth.models import AbstractBaseUser #standard per customizzare i modelli standard
from django.contrib.auth.models import PermissionsMixin#// standard per customizzare i modelli standard
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("USers must have anemail address")
        email = self.normalize_email(email)#mette la second ametà a lower AbstractBaseUser
        user = self.model(email=email, name=name )

        user.set_password(password)# così converte la psw in hash senza metetrla nel database in chiaro
        user.save(using=self._db)

        return user

    def create_superuser(self,email, name, password):
        """cretae a new superuser  with given details"""
        user=self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in te hsystem"""
    email=models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    def __str__(self):
        """return a string represnetation of user"""
        return self.email

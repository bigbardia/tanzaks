from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
import uuid


class KarbarManager(BaseUserManager):
    def create_user(self , password=None , is_admin = False , is_staff = False , is_active = True , username = None):
        if not username:
            return ValueError("username is needed")
        
        user = self.model(username = username)
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using = self._db)
        return user


    def create_superuser(self , username= None , password = None):
        if not username:
            return ValueError("Username in needed")
        
        user = self.model(username = username)
        user.admin ,  user.staff , user.active = True , True  , True
        user.set_password(password)
        user.save(using = self._db)
        return user



class Karbar(AbstractBaseUser):

    username = models.CharField(max_length=48 , unique=True)
    meme_id       = models.UUIDField(primary_key=True , unique=True , editable=False , default=uuid.uuid4,blank=True)

    
    
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = KarbarManager()

    USERNAME_FIELD = "username"



    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active



    def __str__(self):
        return self.username

    def has_module_perms(self , app_label):
        return self.admin

    def has_perm(self, perm, obj=None):
        return self.admin

    def save(self , *args , **kwargs):
        if self.is_admin:
            return super().save(*args , **kwargs)
        super().save(*args , **kwargs)
        self.set_password(str(self.meme_id))
        return super().save(*args , **kwargs)


from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models 

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, password=None, **kwargs):        
        
        if not email :            
            raise ValueError('must have user nickname')        
        user = self.model(            
            email = self.normalize_email(email), **kwargs       
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email,password,**kwargs):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 
        
class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    user_probability = models.CharField(max_length=80, default='0')

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'email'    

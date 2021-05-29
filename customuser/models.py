from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, bio, Approvals, Declines, Comments,password= None, ):
        if not email:
            raise ValueError("Users must have an email adress!")
        if not username:
            raise ValueError("Users must have an username!")
        if not first_name:
            raise ValueError("Users must have a first name!")
        if not last_name:
            raise ValueError("Users must have a last name!")
        # if not profile_picture:
        #     raise ValueError("Users must have a profile picture!")
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            bio= bio,
            Approvals = Approvals,
            Declines = Declines,
            Comments = Comments
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, password, first_name,last_name, bio, Approvals, Declines, Comments):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            bio = bio,
            Approvals = Approvals,
            Declines = Declines,
            Comments = Comments
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name= "email", max_length= 255, unique= True)
    username = models.CharField(max_length= 255, unique= True)
    first_name = models.CharField(max_length= 250)
    last_name = models.CharField(max_length= 255)
    bio = models.TextField(max_length= 3000, default="", blank=True)
    photo = models.ImageField(verbose_name= "user_image", default="userdefault.png")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add= True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now= True)
    is_admin = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)
    Approvals = models.ManyToManyField('backend.Approval', blank= True)
    Declines = models.ManyToManyField('backend.Decline', blank= True)
    Comments = models.ManyToManyField('backend.Comment', blank= True)
    
    
    

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "username"
    REQUIRED_FIELDS = ['email','first_name','last_name']
    
    objects = AccountManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    
class UserImage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_image")
    image = models.ImageField(verbose_name= "image",
                              help_text= "Upload a post image",
                              upload_to="images/",
                              default="userdefault.png",
                              max_length=2000)
    class Meta:
        verbose_name = "User Image"
        verbose_name_plural = "User Images"
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=20,null=True,blank=True)
    mobileNumber = models.CharField(max_length=11,null=True,blank=True)
    profileImage = models.ImageField(upload_to="user/images",null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    class Meta:
        verbose_name_plural = 'Authenticated User'
        
# User Profile
class Profile(models.Model):
    profile = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    address = models.TextField(default="Bandarban")
    # profileImage = models.ImageField(upload_to="user/images", blank=True,null=True)
    
    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"

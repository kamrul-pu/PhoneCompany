from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.full_name}"


from django.db import models
# import re

# class User(models.Model):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     age = models.IntegerField(null = True)
#     location = models.TextField(null = True)
#     email = models.EmailField(max_length=255)
#     phone_number = models.IntegerField(null= True)
#     password = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


# class Program(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     price = models.IntegerField
#     location = models.CharField(max_length=255)
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     interested_users = models.ManyToManyField(User, related_ame="desired_programs")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

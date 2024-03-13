from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length = 100)
    Price = models.IntegerField()
    Rating = models.IntegerField()
    Quantity = models.IntegerField()
    Description = models.CharField(max_length = 1000)
    Live = models.BooleanField()

class Buyer(models.Model):
    Name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 200)
    PhoneNumber = models.CharField(max_length = 10)
    Username = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 10)  

class Seller(models.Model):
    Name = models.CharField(max_length = 100)
    PhoneNumber = models.CharField(max_length = 10)
    Username = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 10)     

     
     
    


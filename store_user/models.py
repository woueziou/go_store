from django.contrib.auth.models import User
from django.db import models

class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    pass

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity_left = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    pass


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(StoreUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    pass



class ProductEvaluation(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(StoreUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    pass


class OrderProducts(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    pass


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    pass



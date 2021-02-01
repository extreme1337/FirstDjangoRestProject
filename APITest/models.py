from django.db import models


# Create your models here.
class Item(models.Model):
    itemID = models.AutoField(primary_key=True, default=1)
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)
    charity = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.item_name


class CharityRegistration(models.Model):
    email = models.EmailField()
    charity_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.charity_name


class UserRegistration(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=200)
    charity_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class OrderedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    username = models.EmailField()

    def __str__(self):
        return self.item_name

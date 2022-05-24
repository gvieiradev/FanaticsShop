from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class Client(models.Model):
    direction = models.CharField(max_length=50)
    phone = models.IntegerField()
    country = models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return self.direction
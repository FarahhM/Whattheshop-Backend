from django.db import models
#from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True, blank=True) 
    gender = models.TextField()
    def __str__(self):
        return self.name
        

# class Preorders(models.Model):
#    name = models.ForeignKey(Item,on_delete=models.CASCADE)
#    user = models.Foreignkey(User,on_delete=models.CASCADE)
   

# class Userchoose(models.Model):
#      name = models.ForeignKey(Preorders,on_delete=models.CASCADE)
#      number = models.IntegerField()


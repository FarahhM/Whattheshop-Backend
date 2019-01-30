from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

GENDER_CHOICES = (
    ('---','__'),
    ('Men','MEN'),
    ('Women','WOMEN'),
    ('Kids','KIDS'),
)
# SIZE_CHOICES = (('---','___'),('Small','Small'),('Medium','Medium'),('Larg','Larg'),
# )
class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True, blank=True) 
    gender = models.CharField(max_length=33,choices=GENDER_CHOICES,default='---')
    


    def __str__(self):
        return self.name

class Previoseorders(models.Model): 
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date = models.DateField(default=datetime.today)
     #totalprice =  

  

       
class Userchocie(models.Model):
      user =models.ForeignKey(Previoseorders,on_delete=models.CASCADE)
      item = models.ForeignKey(Item,on_delete=models.CASCADE)
      size = models.CharField(max_length=120)
      quantity = models.IntegerField()




   
 





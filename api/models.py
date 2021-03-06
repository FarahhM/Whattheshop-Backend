from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, tzinfo
from django.utils.timezone import utc

GENDER_CHOICES = (
    ('---','__'),
    ('Men','MEN'),
    ('Women','WOMEN'),
    ('Kids','KIDS'),
)
TYPE_CHOICES = (
     ('---','__'),
   ('TShirts','tShirts'),
   ('Sunglasses','sunglasses'),
   ('Shoes','shoes'),)
# SIZE_CHOICES = (('---','___'),('Small','Small'),('Medium','Medium'),('Larg','Larg'),
# )
class Classification(models.Model):
   name = models.CharField(max_length=120)
   backgroundImage = models.ImageField(null=True, blank=True)

   def __str__(self):
        return self.name


class Item(models.Model):
    classification = models.ForeignKey(Classification,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True, blank=True) 
    # gender = models.CharField(max_length=33,choices=GENDER_CHOICES,default='---')
    _type = models.CharField(max_length=33,choices=TYPE_CHOICES,default='---')
    
    def __str__(self):
        return self.name

class Previoseorders(models.Model): 

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def total(self):
        total = 0
        #return total
        choices = self.userchoice_set.all()
        for x in choices : 
          total += (x.quantity*x.item.price)
        return  total

    def save(self, *args, **kwargs):
        self.time = datetime.utcnow().replace(tzinfo=utc) + timedelta(hours=3) 
        super(Previoseorders, self).save(*args, **kwargs)
        #self.time =forms.TimeInput(format='%H:%M')
       
    

class Userchoice(models.Model):
      user =models.ForeignKey(Previoseorders,on_delete=models.CASCADE)
      item = models.ForeignKey(Item,on_delete=models.CASCADE)
      size = models.CharField(max_length=120)
      quantity = models.IntegerField()



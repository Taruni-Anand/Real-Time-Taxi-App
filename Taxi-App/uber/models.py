from django.db import models
from django.utils import timezone
# Create your models here.

class Ride(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Link to another model
    title = models.CharField(max_length=200) #Limited number of chars
    text = models.TextField() #Unlimited number of chars
    rider_date = models.DateTimeField(default = timezone.now)
    ride_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.ride_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

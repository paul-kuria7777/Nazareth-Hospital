from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    emergency = models.CharField(max_length=15)
    address = models.CharField(max_length=20)   
    birth = models.DateField()
    role = models.CharField(max_length=12)
    email_confirmed = models.BooleanField(default=False)
    last_login = models.DateField(null=True)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.user.username

class Appointments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_appointment')
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctor_appointment')
    date = models.DateField()
    
    def save_appointment(self):
        self.save()

    def delete_appointment(self):
        self.delete()
    
    def __str__(self):
        return self.user.username
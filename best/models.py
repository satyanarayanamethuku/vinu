from django.db import models
from django.urls import reverse

# Create your models here.


class ApplicationFormClass(models.Model):
    firstName     = models.CharField(max_length=100)
    lastName      = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=False)
    board         = models.CharField(max_length=20, default=False)
    fatherName    = models.CharField(max_length=100)
    motherName    = models.CharField(max_length=100)
    qualification = models.CharField(max_length=30)
    schoolName    = models.CharField(max_length=30)
    schoolAddress = models.CharField(max_length=200)
    homeAddress   = models.CharField(max_length=200)
    state         = models.CharField(max_length=30)
    aadharNumber  = models.CharField(max_length=100)
    phoneNumber   = models.CharField(max_length=100)
    emailID       = models.EmailField(max_length=40)
    username      = models.CharField(max_length=30, unique=True)
    referral      = models.CharField(max_length=254)
    status        = models.CharField(max_length=64)
    date          = models.CharField(max_length=64)
    mail_sent     = models.CharField(default='no', max_length=64)
    
    
    
    def __str__(self):
        return self.firstName

    
    # class Meta:
    #     ordering = ['firstName']

    def get_absolute_url(self):
        return reverse('display_view')
    
    


class Contact(models.Model):
    name  = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=64)
    subject = models.CharField(max_length=254)
    message =models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Bhim_App(models.Model):
    transactionid = models.CharField(max_length=64)
    phoneNumber   = models.CharField(max_length=64)
    email         = models.EmailField(max_length=64)
    full_name     = models.CharField(max_length=64)

    def __str__(self):
        return self.transactionid

    
class Quiz(models.Model):
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20)
    option2 = models.CharField(max_length = 20)
    option3 = models.CharField(max_length = 20)
    option4 = models.CharField(max_length = 20)
    answer = models.CharField(max_length = 25)


    def __str__(self):
        return self.question

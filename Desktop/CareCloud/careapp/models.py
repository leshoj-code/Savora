from django.db import models

# Create your models here.

class patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField()
    medicalhistory = models.TextField()

    def __str__(self):
            return self.firstname
    

class doctor(models.Model):
      firstname = models.CharField(max_length=20)
      lastname = models.CharField(max_length=50)
      specialization = models.CharField(max_length=30) 
      phonenumber = models.CharField(max_length=15)

      def __str__(self):
            return self.firstname
    






class MyAppointments(models.Model):
      name = models.CharField(max_length=200)
      email = models.EmailField()
      phone = models.CharField(max_length=20)
      datetime = models.DateTimeField()
      department = models.CharField(max_length=10)
      doctor = models.CharField(max_length=100)
      message = models.TextField()

      def __str__(self):
            return self.name

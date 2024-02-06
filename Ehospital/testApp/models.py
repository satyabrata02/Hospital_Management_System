from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

class Patientinfo(models.Model):
    admissiondate = models.DateTimeField()
    patientid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phonenumber = models.BigIntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    bloodgroup = models.CharField(max_length=10)
    # Any Major disease suffered earlier
    disease = models.CharField(max_length=500)

class Diagnosis(models.Model):
    patientid = models.IntegerField(primary_key=True)
    drname = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=700)
    diagnosis = models.CharField(max_length=500, default='Checkup')
    medicines = models.CharField(max_length=500)
    # Addmission Required?
    addmissionreq = models.CharField(max_length=10)

class Patientbill(models.Model):
    patientid = models.IntegerField(primary_key=True)
    dischargedate = models.DateTimeField()
    days = models.IntegerField()
    # Ward charges/day
    wardcharge = models.FloatField()
    # Doctor's fee
    drfee = models.FloatField()
    # Service charges
    srvcharge = models.FloatField()
    paidamt = models.FloatField(default=0.0)
    totalamt = models.FloatField()
    payment = models.CharField(max_length=10, default='not paid')


class Patientbedadm(models.Model):
    patientid = models.IntegerField(primary_key=True)
    admitdate = models.DateTimeField()
    prelname = models.CharField(max_length=50)
    relrelation = models.CharField(max_length=50)
    prephoneno = models.BigIntegerField()
    roomno = models.CharField(max_length=10)
    assignedstaffs = models.CharField(max_length=50)
    termsorcond = models.CharField(max_length=200)

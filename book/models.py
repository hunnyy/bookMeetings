from django.db import models
from .forms import LoginForm

# Create your models here

class Compadd(models.Model):
	compname=models.CharField(max_length=100, unique=True)
	Credits=models.TextField()

class CompanyRegister(models.Model):
	name = models.CharField(max_length=100)
	Credits = models.CharField(max_length=10)
	DefaultCredits = models.CharField(max_length=10)
	Property = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class RoomAdd(models.Model):
	Roomname = models.CharField(max_length=100)
	CreditsPerHr = models.CharField(max_length=10)
	Capacity = models.CharField(max_length=10)
	Property = models.CharField(max_length=20)

class HrLogin(models.Model):
	Company = models.CharField(max_length=100)
	Name = models.CharField(max_length=200)
	Email = models.EmailField(max_length=300)

class Login(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class LoginUser(LoginForm):
	class Meta:
		model = Login
		fields = ['username','password']

class EventAdd(models.Model):
		Title = models.CharField(max_length=100)
		Event_description = models.CharField(max_length=1000)
		Event_sponsor = models.CharField(max_length=100)
		Event_location = models.CharField(max_length=100)
		Event_date = models.DateTimeField()


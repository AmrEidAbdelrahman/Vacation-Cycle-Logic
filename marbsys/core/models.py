from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.

vacationrequeststatus = (
		('R', 'Rejected'),
		('IR', 'In Review'),
		('A', 'Accepted')
	)


class Employee(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=50)
	hiring_date = models.DateField()
	profile_img = models.ImageField(upload_to="profile_pics", default="default_profile_pic.jpg")
	birth_date = models.DateField()
	mobile_number = models.CharField(max_length=15)
	e_mail = models.EmailField(max_length=50)
	address = models.CharField(max_length=200)


	def __str__(self):
		return f'{self.name}'


	def vacation_days(self):
		'''
		return number of vacation days allowed for the employee
		RULE: if employee is working for more than 10 years in the company then s/he will get 30 days off else will get 21
		'''
		hiring_date = self.hiring_date
		now = datetime.datetime.now()
		difference = now.year - hiring_date.year
		if difference > 10:
			return 30
		return 21


	def taken_days(self):
		taken_vacations = VacationRequest.objects.all().filter(employee=self, status='A')
		days = 0
		for vac in taken_vacations:
			days += (vac.vacation_to - vac.vacation_from).days
		return days


	def remaining_days(self):
		return self.vacation_days() - self.taken_days()




class OfficialVacation(models.Model):
	holiday_name = models.CharField(max_length=100)
	date = models.DateField()


	def __str__(self):
		return f'{self.holiday_name}'



class VacationRequest(models.Model):
	employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
	vacation_from = models.DateField()
	vacation_to = models.DateField()
	reason = models.TextField()
	status = models.CharField(max_length=2, choices=vacationrequeststatus, default="IR")





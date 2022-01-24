from django import forms

from .models import Employee


class VacationRequestForm(forms.Form):
	vacation_from = forms.DateField(widget=forms.SelectDateWidget)
	vacation_to = forms.DateField(widget=forms.SelectDateWidget)
	reason = forms.CharField(widget=forms.Textarea(attrs={"style": "resize: none"}))


class EmployeeCreateForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['name', 'job_title', 'hiring_date', 'birth_date', 'mobile_number', 'e_mail', 'address', 'profile_img']


class EmployeeUpdateForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['name', 'job_title', 'hiring_date', 'birth_date', 'mobile_number', 'e_mail', 'address', 'profile_img']



from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.http import QueryDict
from django.contrib import messages

import datetime

from .models import Employee, VacationRequest, OfficialVacation
from .forms import VacationRequestForm, EmployeeCreateForm, EmployeeUpdateForm
# Create your views here.



class EmployeeView(View):
	def get(self, request, *args, **kwargs):
		employee = Employee.objects.all()
		create_form = EmployeeCreateForm()
		context = {
			'test':"test",
			'employees': employee,
			'create_form': create_form
		}
		return render(request, 'core/employee_data_table.html', context)


	def post(self, request, *args, **kwargs):
		form = EmployeeCreateForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			form.save()
			employees = Employee.objects.all()
			data = serializers.serialize("json", Employee.objects.all())

		return JsonResponse({"message": "THE REQIEST HAS BEEN SBMITED", "employees":data}, status=200)


	def put(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		employee = Employee.objects.get(pk=pk)
		put = QueryDict(request.body)
		form = EmployeeUpdateForm(put, instance=employee)
		if form.is_valid():
			form.save()
		else:
			# TODO: handel errors
			print(form.errors)
		employees = Employee.objects.all()
		data = serializers.serialize("json", Employee.objects.all())

		return JsonResponse({"message": "THE REQIEST HAS BEEN SUBMITED", "employees":data}, status=200)


	def delete(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		employee = Employee.objects.get(pk=pk)
		employee.delete()
		employees = Employee.objects.all()
		data = serializers.serialize("json", Employee.objects.all())
		return JsonResponse({}, status=200)




class VacationView(View):
	def get(self, request, *args, **kwargs):
		form = VacationRequestForm()
		pk = self.kwargs['pk']
		employee = Employee.objects.get(pk=pk)
		vacations_requests = VacationRequest.objects.all().filter(employee=employee)
		have_ir = True if vacations_requests.filter(status='IR').count() > 0 else False
		print(have_ir)
		context = {
			'form': form,
			'employee': employee,
			'vacations_requests':vacations_requests,
			'have_ir':have_ir
		}
		return render(request, 'core/vacation_request.html', context)


	def post(self, request, *args, **kwargs):
		form = VacationRequestForm(request.POST)
		pk = self.kwargs['pk']
		employee = Employee.objects.get(pk=pk)
		if form.is_valid():
			vacation_from = form.cleaned_data["vacation_from"]
			vacation_to = form.cleaned_data["vacation_to"]
			reason = form.cleaned_data["reason"]
			days = (vacation_to - vacation_from).days + 1
			from_datetime = datetime.datetime(vacation_from.year, vacation_from.month, vacation_from.day)
			print(datetime.datetime(vacation_from.year, vacation_from.month, vacation_from.day))
			
			if vacation_from > vacation_to:
				return JsonResponse({"message": "wronge date selection"}, status=200)

			
			if days > 1:
				print("this system doesn't allow ask more than one day !")
				return JsonResponse({"message": "this system doesn't allow ask more than one day !"}, status=200)
			elif days == 1:
				# is there any conflict between the asked day and the official vacation days ?
				oficial_days = OfficialVacation.objects.all().filter(date__gte=from_datetime, date__lte=from_datetime).count()
				if oficial_days > 0 :
					return JsonResponse({"message":"this day is an official vacation already"}, status=200)


			vacation_request = VacationRequest(employee=employee, vacation_from=vacation_from, vacation_to=vacation_to, reason=reason)
			vacation_request.save()
			return JsonResponse({}, status=200)
				
		else:
			print("######WRONG DATA#########")
			## TODO: handeled in frontend
			return JsonResponse({"error": form.errors}, status=400)
		
		return JsonResponse({"error": "something went wrong"}, status=400)



def get_edit_form(request, pk):
	employee = Employee.objects.get(pk=pk)
	form = EmployeeUpdateForm(instance=employee)
	context = {
	"form": form,
	}
	template = render_to_string('core/form.html', context=context)
	return JsonResponse({"form": template})
from django.contrib import admin
from .models import Employee, OfficialVacation, VacationRequest
# Register your models here.

admin.site.register(Employee)
admin.site.register(OfficialVacation)
admin.site.register(VacationRequest)

from django.urls import path

from .views import EmployeeView, VacationView, get_edit_form


urlpatterns = [
	path('', EmployeeView.as_view(), name="home-page"),
	path('delete-employee/<pk>/', EmployeeView.as_view(), name="employee-delete"),
	path('employee-edit/<pk>/', EmployeeView.as_view(), name="employee-edit"),
	path('edit-employee/<pk>/', get_edit_form, name="get-edit-form"),


	path('vacation-request/<pk>/', VacationView.as_view(), name="vacation-request"),


]
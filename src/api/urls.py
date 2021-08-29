from django.urls import path

from . import views

urlpatterns = [
    path("department/", views.DepartmentView.as_view()),
    path("department/<int:pk>", views.DepartmentView.as_view()),
    path("employee/", views.EmployeeView.as_view()),
    path("employee/<int:department_pk>", views.EmployeeView.as_view()),
    path("task/", views.TaskView.as_view()),
    path("task/<int:pk>", views.TaskView.as_view()),
]

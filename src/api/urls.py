from django.urls import path
from opt_einsum import paths
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('user', views.UserViewSet, 'user')

urlpatterns = [
    path("department/", views.DepartmentView.as_view()),
    path("department/<int:pk>", views.DepartmentView.as_view()),
    path("employee/", views.EmployeeView.as_view()),
    path("employee/<int:department_pk>", views.EmployeeView.as_view()),
    path("task/", views.TaskView.as_view()),
    path("task/<int:pk>", views.TaskView.as_view()),
    path("auth/login/", views.Auth.as_view({"post": "login"})),
    path("auth/register/", views.Auth.as_view({"post": "register"})),
    path("task/notassignedtask/", views.NotAssignedTask.as_view()),
    path("employee/get_free_employee/<int:department_id>", views.EmployeeViewGetFree.as_view()),
    *router.urls,
]

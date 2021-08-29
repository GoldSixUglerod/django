from django.urls import path

from . import views

urlpatterns = [
    path("task/", views.DepartmentView.as_view()),
    path("talk/<int:pk>", views.DepartmentView.as_view()),
]

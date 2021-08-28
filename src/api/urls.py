from django.urls import path

import ai_api
from . import views

urlpatterns = [
    path("department/", views.DepartmentView.as_view()),
    path("department/<int:pk>", views.DepartmentView.as_view()),


]

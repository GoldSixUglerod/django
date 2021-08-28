from django.urls import path

import ai_api
from . import views

urlpatterns = [
    path("action/", views.ActionView.as_view()),
    path("action/<int:pk>", views.ActionView.as_view()),
]

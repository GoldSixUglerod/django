from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Employee, Leader, Action, Task


class TaskView(APIView):
    def get(self, request, pk):
        pass

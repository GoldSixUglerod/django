from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee, Leader
from .serializers import EmployeeSerializer


class EmployeeView(APIView):
    def get(self, request, pk):
        pass

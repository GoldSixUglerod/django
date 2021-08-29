from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import EmployeeSerializer
from ..models import Employee, Leader, Department
import requests

from ..models import Department, Employee, Leader


class EmployeeView(APIView):
    def get(self, request, department_pk):
        res = {}
        employees = Employee.objects.filter(department_id=department_pk)
        root = employees.get(main=True)

        res['name'] = str(root.user.last_name) + str(root.user.first_name)
        res['attributes'] = root.to_json()
        res['children'] = []
        children_id = Leader.objects.filter(leader_id=root.pk)

        if children_id.count() > 0:
            DFS(res, children_id, employees)
        print(res)
        return Response(res)

    @action(methods=["GET"], detail=True)
    def get_employee_by_username(self, request, username):
        data = request.data
        first, second = username.split(" ")

        employee = Employee.objects.filter(user__first_name = first, user__last_name = second).first()
        if not employee:
            employee = Employee.objects.filter(user__first_name = second, user__last_name = first).first
            if not employee:
                return Response({"status": "error","description": "No such user"})


        return Response(employee.get_json())




    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_employees = serializer.save()
            return Response({"status": "success", "description": f"Employee '{saved_employees}' created successfully"})
        return Response({"status": "error", "desription": "Validate error"})

    def path(self, request):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data

        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_employee = serializer.save()
            return Response(
                {
                    "status": "success",
                    "desciption": f"Employee '{saved_note}' updated successfully",
                }
            )
        return Response({"status": "error", "desription": "Validate error"})

    def delete(self, request, pk):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({"success": f"Employee with id '{pk}' has been deleted."})


def DFS(res, children_id, employees):
    for i in range(children_id.count()):
        tmp_employee = employees.get(pk=children_id[i].employee_id)
        res['children'].append({'name': str(root.user.last_name) + str(root.user.first_name), 'attributes': tmp_employee.to_json(),
                                'children': []})
        leaders = Leader.objects.filter(leader_id=tmp_employee.pk)
        if leaders.count() != 0:
            DFS(res['children'][i], leaders, employees)

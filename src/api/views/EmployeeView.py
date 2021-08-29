from django.shortcuts import render
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

        res['name'] = root.user.username
        res['attributes'] = root.to_json()
        res['children'] = []
        children_id = Leader.objects.filter(leader_id=root.pk)

        if children_id.count() > 0:
            DFS(res, children_id, employees)
        print(res)
        return Response(res)

    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_employees = serializer.save()
            return Response({"status": "success", "description": f"Employee '{saved_employees}' created successfully"})
        return Response({"status": "error", "desription": "Validate error"})

    def path(self, request):
        pass





def DFS(res, children_id, employees):
    for i in range(children_id.count()):
        tmp_employee = employees.get(pk=children_id[i].employee_id)
        res['children'].append({'name': tmp_employee.user.username, 'attributes': tmp_employee.to_json(),
                                'children': []})
        leaders = Leader.objects.filter(leader_id=tmp_employee.pk)
        if leaders.count() != 0:
            DFS(res['children'][i], leaders, employees)

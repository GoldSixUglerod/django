from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Employee, Leader, Department


class EmployeeView(APIView):
    def get(self, request, department_pk):
        res = {}
        employees = Employee.objects.filter(department_id=department_pk)
        root = employees.get(main=True)
        res['name'] = root.name
        res['attributes'] = root
        res['children'] = []
        children_id = Leader.objects.filter(leader_id=root.id).values_list('employee_id')
        if children_id.count() > 0:
            DFS(res, children_id, employees)
        return res


def DFS(res, children_id, employees):
    for i in range(children_id.count()):
        tmp_employee = employees.get(children_id[i][0])
        res['children'].append({'name': tmp_employee['name'], 'attributes': tmp_employee, 'children': []})
        leaders = Leader.objects.filter(leader_id=tmp_employee.id).values_list('employee_id').count()
        if leaders != 0:
                DFS(res['children'][i], leaders, employees)

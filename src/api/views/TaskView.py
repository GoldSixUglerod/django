from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import TaskSerializer

from ai_api.utils import KeywordsExtractor, vectorize_words
from ..models import Employee, Leader, Department, Task


class TaskView(APIView):
    def get(self, request, pk):
        task = Task.objects.all()
        serializer = TaskSerializer(task)
        return Response({"task": serializer.data})

    def post(self, request):
        data = request.data

        description = data['description']
        if description == "" or description is None:
            return Response({'status': 'error', 'description': "You have to provide a description"})

        list_targets = KeywordsExtractor().extract(description)

        data['list_targets'] = list_targets
        data['name'] = " ".join(list_targets)

        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response({"status": "success", "description": f"Task '{saved_note}' created successfully"})
        return Response({"status": 'error', 'description': "Validate error"})

    def patch(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data

        if data['list_targets']:
            return Response({'status': 'error', 'description': "You can't change and list_targets of task"})

        serializer = TaskSerializer(instance=saved_task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_task = serializer.save()
            return Response({"status": "success", "desciption": f"Task '{saved_task}' updated successfully"})
        return Response({"status": "error", "desription": "Validate error"})

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({"success": f"Task with id '{pk}' has been deleted."})

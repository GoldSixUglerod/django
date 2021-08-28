from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import TaskSerializer
from datetime import date, timedelta

from ai_api.utils import KeywordsExtractor, vectorize_words
from ..models import Employee, Leader, Department, Task


class TaskView(APIView):
    def get(self, request, pk):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks)
        return Response({"tasks": serializer.data})

    def post(self, request):
        description = request.data.get("description")
        end_time_best_req = request.data.get("end_time_best", {})
        end_time_actual = None
        finished = False
        score = None


        if description is None:
            return Response({"status": "error", "description": "No description passed"})

        list_targets = KeywordsExtractor().extract(description)
        name = " ".join(list_targets)
        end_time_best = date.today() + timedelta(days=3)
        if "year" in end_time_best_req and "month" in end_time_best_req and "day" in end_time_best_req:
            end_time_best = date(
                year=end_time_best_req["year"], month=end_time_best_req["month"], day=end_time_best_req["day"])

        data = {
            "name": name,
            "description": description,
            "list_targets": list_targets,
            "end_time_best": end_time_best,
            "end_time_actual": end_time_actual,
            "finished": finished,
            "score": score
        }

        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # TODO Assign task on department/employee

            saved_note = serializer.save()
            return Response({"status": "success", "description": f"Task \"{saved_note}\" created successfully"})

    def patch(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data

        if data["list_targets"]:
            return Response({"status": "error", "description": "You can't change and list_targets of task"})

        serializer = TaskSerializer(instance=saved_task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_task = serializer.save()
            return Response({"status": "success", "desciption": f"Task \"{saved_task}\" updated successfully"})
        return Response({"status": "error", "desription": "Validate error"})

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({"success": f"Task with id \"{pk}\" has been deleted."})

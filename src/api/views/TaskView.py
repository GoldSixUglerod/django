from datetime import date, timedelta

from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

<<<<<<< HEAD
from ai_api.utils import KeywordsExtractor, vectorize_words
from ..models import Employee, Leader, Department, Task
from ai_api import utils
=======
from ai_api.utils import KeywordsExtractor, download_model, vectorize_words
>>>>>>> 4f0ef54f865cd502093ce88ffddef995758d54eb
from config import DEFAULT_DEPARTMENT_CHOOSE_THRESHOLD

from ..models import Department, Employee, Leader, Task
from ..serializers import TaskSerializer


w2v_model = utils.download_model()


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})

    def post(self, request):
        description = request.data.get("description")
        end_time_best_req = request.data.get("end_time_best", {})
        department_choose_threshold = request.data.get(
            "department_choose_threshold", DEFAULT_DEPARTMENT_CHOOSE_THRESHOLD
        )
        end_time_actual = None
        finished = False
        score = None

        if description is None:
            return Response({"status": "error", "description": "No description passed"})

        list_targets, confidences = KeywordsExtractor().extract(description)
        name = " ".join(list_targets)
        end_time_best = date.today() + timedelta(days=3)
        if (
            "year" in end_time_best_req
            and "month" in end_time_best_req
            and "day" in end_time_best_req
        ):
            end_time_best = date(
                year=end_time_best_req["year"],
                month=end_time_best_req["month"],
                day=end_time_best_req["day"],
            )
        expected_period_days = (end_time_best - date.today()).days

        data = {
            "name": name,
            "description": description,
            "list_targets": list_targets,
            "end_time_best": end_time_best,
            "expected_period_days": expected_period_days,
            "end_time_actual": end_time_actual,
            "finished": finished,
            "score": score,
            "employee": None,
        }
        department_confidences, departments = self.get_department_confidences(
            list_targets, confidences
        )

        if max(department_confidences) < department_choose_threshold:
            serializer = TaskSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                saved_note = serializer.save()
            return Response(
                {
                    "status": "need action",
                    "description": f"Choosing department model cannot confidently define department to choose for task {saved_note}",
                    "variants": [
                        {
                            "department": departments[dep_index].name,
                            "probability": department_confidences[dep_index],
                        }
                        for dep_index in range(len(departments))
                    ],
                }
            )

        choosen_department = departments[
            department_confidences.index(max(department_confidences))
        ]
        employees = Employee.objects.filter(
            department=choosen_department, status="active"
        )
        if len(employees):
            return Response(
                {
                    "status": "need action",
                    "description": f"No active employee in selected department {choosen_department}",
                }
            )
        employees_busyness = []
        for employee in employees:
            emp_tasks = Task.objects.filter(employee=employee)
            tasks_required_time = (
                sum([task.expected_period_days for task in emp_tasks])
                + expected_period_days
            )
            done_tasks = emp_tasks.filter(finished=True)
            emp_score = 5
            if len(done_tasks) > 0:
                emp_score = sum([task.score for task in done_tasks]) / len(done_tasks)
            emp_busyness = tasks_required_time / (emp_score ** 0.5)
            employees_busyness.append(emp_busyness)
        chosen_employee = employees[employees.index(min(employees_busyness))]

        data["employee"] = chosen_employee

        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response({"status": "success", "description": f"Task '{saved_note}' created successfully"})
        return Response({"status": 'error', 'description': "Validate error"})

    def patch(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data

        if data["list_targets"]:
            return Response(
                {
                    "status": "error",
                    "description": "You can't change and list_targets of task",
                }
            )

        serializer = TaskSerializer(instance=saved_task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_task = serializer.save()
            return Response(
                {
                    "status": "success",
                    "desciption": f'Task "{saved_task}" updated successfully',
                }
            )
        return Response({"status": "error", "desription": "Validate error"})

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({"success": f'Task with id "{pk}" has been deleted.'})

    def get_department_confidences(self, keywords, kw_confidences):
        sum_squared_words_confses = sum([conf ** 2 for conf in kw_confidences])
        words_normalized_coefficients = [
            conf ** 2 / sum_squared_words_confses for conf in kw_confidences
        ]
        departments = Department.objects.all()
        department_confidences = []
        extracted_target = [tg.replace("ё", "е") for tg in utils.word2vector.add_target(keywords)]
        for department in departments:
            dep_conf = 0
            employees_target = [tg.replace("ё", "е") for tg in utils.word2vector.add_target(department.list_targets)]
            for task_word_index in range(len(keywords)):
                task_word = extracted_target[task_word_index]
                max_similarity = 0
                for dep_word in employees_target:
                    similarity = 0
                    try:
                        similarity = w2v_model.similarity(task_word, dep_word)
                    except KeyError:
                        print("KeyError")
                        pass
                    if similarity > max_similarity:
                        max_similarity = similarity
<<<<<<< HEAD
                    print(utils.word2vector.add_target([task_word])[0], utils.word2vector.add_target([dep_word])[0], similarity)
                dep_conf += max_similarity * words_normalized_coefficients[task_word_index]
=======
                dep_conf += (
                    max_similarity * words_normalized_coefficients[task_word_index]
                )
>>>>>>> 4f0ef54f865cd502093ce88ffddef995758d54eb
            department_confidences.append(dep_conf)
        return department_confidences, departments


class NotAssignedTask(APIView):
    def get(self, request):
        tasks = Task.objects.filter(employee=None)
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})
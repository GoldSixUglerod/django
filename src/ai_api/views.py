from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.Department import Department
from .utils import vectorize_words
from .utils import KeywordsExtractor


class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DeparmentSerializer(departments, many=True)
        return Response({"departments": serializer.data})

    def post(self, request):
        description = request.data.get("description")

        if description is None:
            return Response({"error": f"No name passed"})

        keywords, confidences = KeywordsExtractor().extract(description)
        keywords_vectorized = vectorize_words(keywords)
        name = " ".join(keywords)

        # Create an object on got data
        department = {
            "name": name,
            "keywords": keywords,
            "keywords_vectorized": keywords_vectorized,
            "description": description
        }

        serializer = TaskSerializer(data=action)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response({"success": f"Task '{saved_note}' created successfully"})
    #
    # def put(self, request, pk):
    #     saved_note = get_object_or_404(Note.objects.all(), pk=pk)
    #     data = request.data.get("note")
    #     serializer = NoteSerializer(instance=saved_note, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         saved_note = serializer.save()
    #         return Response({"success": f"Note '{saved_note}' updated successfully"})
    #
    # def delete(self, request, pk):
    #     note = get_object_or_404(Note.objects.all(), pk=pk)
    #     note.delete()
    #     return Response({"success": f"Note with id '{pk}' has been deleted."})

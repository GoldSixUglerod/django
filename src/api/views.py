from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from


class EmployeeView(APIView):
    def get(self):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response({"notes": serializer.data})
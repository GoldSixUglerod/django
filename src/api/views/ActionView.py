from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from ..models import Action
from ..serializers import ActionSerializer

from src.ai_api.utils import vectorize_words
from src.ai_api.utils import KeywordsExtractor
from rest_framework.views import APIView
from rest_framework.response import Response


class ActionView(APIView):
    def get(self, request):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response({"actions": serializer.data})

    def post(self, request):
        description = request.data.get("description")

        if description is None:
            return Response({"error": f"No name passed"})

        keywords = KeywordsExtractor().extract(description)
        print("MMMMM keywords", keywords)
        keywords_vectorized = vectorize_words(keywords)
        name = " ".join(keywords)

        # Create an object on got data
        action = {
            "name": name,
            "keywords": keywords,
            "keywords_vectorized": keywords_vectorized,
            "description": description
        }
        print("BBBBB action", action)

        serializer = ActionSerializer(data=action)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response({"success": f"Action '{saved_note}' created successfully"})
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

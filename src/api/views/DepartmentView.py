from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Department
from ..serializers import DepartmentSerializer


class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response({"departments": serializer.data})

    def post(self, request):
        data = request.data

        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response(
                {
                    "status": "success",
                    "description": f"Department '{saved_note}' created successfully",
                }
            )
        return Response({"status": "error", "desription": "Validate error"})

    def patch(self, request, pk):
        saved_note = get_object_or_404(Department.objects.all(), pk=pk)
        data = request.data

        serializer = DepartmentSerializer(instance=saved_note, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_note = serializer.save()
            return Response(
                {
                    "status": "success",
                    "desciption": f"Department '{saved_note}' updated successfully",
                }
            )
        return Response({"status": "error", "desription": "Validate error"})

    def delete(self, request, pk):
        note = get_object_or_404(Department.objects.all(), pk=pk)
        note.delete()
        return Response({"success": f"Note with id '{pk}' has been deleted."})



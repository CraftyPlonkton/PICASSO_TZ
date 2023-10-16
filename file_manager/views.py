from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response

from file_manager.models import File
from file_manager.serializers import FileSerializer
from file_manager.tasks import file_handling_task


@api_view(['POST',])
def file_upload(request, *args, **kwargs):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        file_handling_task.delay(instance.id)
        return Response(serializer.data, HTTPStatus.CREATED)
    return Response(serializer.errors, HTTPStatus.BAD_REQUEST)


@api_view(['GET',])
def file_list(request, *args, **kwargs):
    queryset = File.objects.all()
    serializer = FileSerializer(queryset, many=True)
    return Response(serializer.data, HTTPStatus.OK)

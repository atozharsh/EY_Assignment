from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import AddNumbersSerializer, ResponseDataSerializer

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets


# views.py
def validate_payload(payload):
    if all([type(i) == list for i in payload]):
        for e in payload:
            if not all([isinstance(i, (int, float)) for i in e]):
                return False
        return True
    return False

class AddNumbersViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny,]
    serializer_class = AddNumbersSerializer

    def create(self, request):
        started_at = datetime.now()
        exec_status = 'running'
        try:
            serializer = AddNumbersSerializer(data=request.data)
            print(request.data)
            print(serializer.is_valid())
            if serializer.is_valid():
                batch_id = serializer.validated_data.get('batchid')
                numbers_list = serializer.validated_data.get('payload')
                if not batch_id:
                    return Response('Missing Batch ID', status=status.HTTP_400_BAD_REQUEST)
                if not validate_payload(numbers_list):
                    return Response('Invalid Input Payload Format', status=status.HTTP_400_BAD_REQUEST)
                response = [sum(nums) for nums in numbers_list]

                exec_status = 'completed'
                completed_at = datetime.now()

                response_data = {
                    "batchid": batch_id,
                    "response": response,
                    "status": exec_status,
                    "started_at": started_at,
                    "completed_at": completed_at
                }
                print(response_data)
                response_serializer = ResponseDataSerializer(data=response_data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
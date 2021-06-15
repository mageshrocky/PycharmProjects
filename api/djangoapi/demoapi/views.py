from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serialize_data = EmployeeSerializers(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getting_data(request):
    x = request.GET.get('name', None)
    record = Employee.objects.all()
    result = EmployeeSerializers(record, many=True)
    return Response(result.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_record(request):
    try:
        record = Employee.objects.get(name='tharun')
    except Exception as e:
        print(e)
    result = EmployeeSerializers(record, data=request.data)
    if result.is_valid():
        result.save()
        return Response(result.data, status=status.HTTP_200_OK)

    return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def del_record(request):
    try:
        y = request.GET.get('name', None)
        record = Employee.objects.get(name=y)
    except Exception as e:
        print(e)
    if record:
        record.is_deleted = True
        record.save()
        return Response("Record Deleted", status=status.HTTP_200_OK)

    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete(request):
    try:
        y = request.GET.get('name', None)
        record = Employee.objects.get(name=y)
    except Exception as e:
        print(e)
    if record:
        record.is_deleted = True
        record.save()
        return Response("Record Deleted", status=status.HTTP_200_OK)

    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getting_delete_data(request):
    record = Employee.objects.filter(is_deleted=True)
    result = EmployeeSerializers(record, many=True)
    return Response(result.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getting_current_data(request):
    record = Employee.objects.filter(is_deleted=False)
    result = EmployeeSerializers(record, many=True)
    return Response(result.data, status=status.HTTP_200_OK)
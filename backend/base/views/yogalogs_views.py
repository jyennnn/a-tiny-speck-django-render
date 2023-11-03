from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User 

from base.models import YogaLogs
from base.serializer import YogaLogsSerializer

from rest_framework import status



@api_view(['GET'])
def getYogaLogs(request): 
    yogaLogs = YogaLogs.objects.all()
    serializer = YogaLogsSerializer(yogaLogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getYogaLogsByUser(request, pk): 
    try:
        yogaLogsByUser = YogaLogs.objects.filter(user=pk)
        serializer = YogaLogsSerializer(yogaLogsByUser, many=True)
        return Response(serializer.data)

    except YogaLogs.DoesNotExist:
        return Response({'message': 'YogaLogs not found for this user'}, status=404)


@api_view(['POST'])
def logYogaPractice(request):
    data = request.data
    
    yogaLog_data = {
        'user': data['user'],
        'reminder': data['reminder'],
        'time': data['time'],
        'completedAt': data['completedAt']
    }
    
    serializer = YogaLogsSerializer(data=yogaLog_data)
    
    if serializer.is_valid():
        serializer.save()  # Save the instance to the database
        return Response(serializer.data, status=201)
    
    else:
        return Response(serializer.errors, status=400)

        
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import URLSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import URL
# Create your views here.
class AllUrls(APIView):
    def get(self,request,format=None):
        queryset = URL.objects.all()
        serializer = URLSerializer(queryset,many=True)
        response_data = serializer.data
        return Response(response_data,status=status.HTTP_200_OK)
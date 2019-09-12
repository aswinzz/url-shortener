from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from .serializers import URLSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import URL
import hashlib
import uuid
from django.conf import settings

class AllUrls(APIView):
    def get(self,request,format=None):
        queryset = URL.objects.all()
        serializer = URLSerializer(queryset,many=True)
        response_data = serializer.data
        return Response(response_data,status=status.HTTP_200_OK)

class URLShortner(APIView):
    def post(self,request,format=None):
        url=request.data.get("url")
        if(not url.__contains__("http")):
            url="http://"+url
        url_unique=str(uuid.uuid4())+url
        hashed_url = hashlib.sha1(url_unique.encode("UTF-8")).hexdigest()
        hashed_url = hashed_url[:7]
        urlObj=URL(short=hashed_url,url=url)
        urlObj.save()
        serializer = URLSerializer(urlObj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetURL(APIView):
    def get(self,request,pk,format=None):
        urlObj=URL.objects.get(short=pk)
        urlObj.clicks+=1
        urlObj.save()
        data={
            "url":urlObj.url
        }
        return Response(data, status=status.HTTP_200_OK)

def RedirectURL(request,pk):
    urlObj=URL.objects.get(short=pk)
    urlObj.clicks+=1
    urlObj.save()
    url=urlObj.url
    return redirect(url)

def home(request,shorturl):
    if request.method == 'GET':
        urls = URL.objects.all().order_by('-clicks')
        return render(request, 'index.html',{"urls":urls}) 
    else:
        url=request.POST["url"]
        if(not url.__contains__("http")):
            url="http://"+url
        url_unique=str(uuid.uuid4())+url
        hashed_url = hashlib.sha1(url_unique.encode("UTF-8")).hexdigest()
        hashed_url = hashed_url[:7]
        urlObj=URL(short=hashed_url,url=url)
        urlObj.save()
        urls = URL.objects.all().order_by('-clicks')
        shorturl=settings.BASE_URL+"/"+urlObj.short
        return render(request, 'index.html',{"shorturl":shorturl,"urls":urls}) 
    


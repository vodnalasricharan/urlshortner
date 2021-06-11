from django.shortcuts import render
from rest_framework import status,request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import urlshorserializer
from django.views.decorators.csrf import csrf_exempt
from .models import *
import random,string
import io
from rest_framework.parsers import JSONParser
import json
# Create your views here.
@api_view(['POST'])
def createurl(request):
    if request.method =='POST':
        data= JSONParser().parse(request)
        try:
            shorturl=urlshort.objects.get(url=data['url'])
            serializer=urlshorserializer(shorturl)
            return Response(serializer.data)
        except:
            while True:
                slug = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
                               for x in range(10))
                try:
                    ret = urlshort.objects.get(slug=slug)
                    continue
                except urlshort.DoesNotExist:
                    break
            data2=dict()
            data2['url']=data['url']
            data2['slug']=slug
            serializer=urlshorserializer(data=data2)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def urlRedirect(request,slugs):
    try:
        ret = urlshort.objects.get(slug=slugs)
    except urlshort.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=urlshorserializer(ret)
    return Response(serializer.data['url'])
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class BlogView(APIView):
    
    def post(self,request):
        try:
            data=request.data
            serializer=Blogserializer(data=data)
            if not serializer.is_valid():
               return Response(
                   {
                       'data':serializer.errors,
                        'message':'something went wrong'},
                        status=status.HTTP_400_BAD_REQUEST
               )
            serializer.save()
            return Response(
                {
                    'data':serializer.data,
                    'message':"blog created sucessfully"
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    'data':'data{}',
                    'message':"something went wrong"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

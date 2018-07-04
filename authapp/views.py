from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .serializers import AlbumSerializer

class ExampleView(APIView):
    # throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        content = {
            'status':'aa' 
        }
        return Response(content)
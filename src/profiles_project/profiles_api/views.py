from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of API views"""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'It gives you the most control over your logic',
            'It maps manually to your URLs'
        ]

        return Response({'message':'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello with with our name"""
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handling the object update"""

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handling only provided updated"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self,request):
        """Create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message':message})

        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """retrieves a particular obj by ID """
        return Response({'httpmethod': 'GET'})

    def update(self,request, pk=None):
        """Handles updating an object"""
        return Response({'httpmethod':'PUT'})

    def partialUpdate(self,request,pk=None):
        """Hanldles partialUpdate"""
        return Response({'httpmethod':'PATCH'})

    def destroy(self,request,pk=None):
        """hanldes removing an Obj"""
        return Response({'httpmethod':'DELETE'})

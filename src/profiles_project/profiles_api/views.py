from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response

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

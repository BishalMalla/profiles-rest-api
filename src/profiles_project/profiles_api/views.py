from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of API views"""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'It gives you the most control over your logic',
            'It maps manually to your URLs'
        ]

        return Response({'message':'hello!', 'an_apiview': an_apiview})

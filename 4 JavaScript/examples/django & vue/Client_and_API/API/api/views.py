from rest_framework import generics
from boletes.models import Bolete
from .serializers import BoleteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

class BoleteAPIView(generics.ListAPIView):
    queryset = Bolete.objects.all()
    serializer_class = BoleteSerializer

class BoleteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Bolete.objects.get(pk=pk)
        except Bolete.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bolete = self.get_object(pk)
        serializer = BoleteSerializer(bolete)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bolete = self.get_object(pk)
        serializer = BoleteSerializer(bolete, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bolete = self.get_object(pk)
        bolete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddBolete(APIView):
    def post(request):
        bolete_data = JSONParser().parse(request)
        bolete_serializer = BoleteSerializer(data=bolete_data)
        if bolete_serializer.is_valid():
            bolete_serializer.save()
            return JsonResponse(bolete_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bolete_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

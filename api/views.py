from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.models import Calculator
from api.serializer import CalculatorSerializer


# Create your views here.



class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = Calculator.objects.all().order_by('-id')
    serializer_class = CalculatorSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

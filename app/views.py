from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
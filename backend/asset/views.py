from django.shortcuts import render
from rest_framework import generics
from .models import Asset, Category, Property
from .serializers import AssetSerializer, CategorySerializer, PropertySerializer

class AssetCreate(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetList(generics.ListAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer

class CategorytDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    

class PropertyCreate(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer    

class PropertyList(generics.ListAPIView):
    queryset =  Property.objects.all()
    serializer_class = PropertySerializer

class PropertytDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer      

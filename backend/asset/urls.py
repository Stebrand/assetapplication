from django.urls import path
from .views import AssetCreate, AssetList, AssetDetail, CategoryCreate, CategoryList, CategorytDetail, PropertyCreate, PropertyList,  PropertytDetail

urlpatterns = [
    path('assets/', AssetList.as_view(), name='asset-list'),
    path('assetcreate/', AssetCreate.as_view()),
    path('asset/<int:pk>/', AssetDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categorycreate/', CategoryCreate.as_view()),
    path('category/<int:pk>', CategorytDetail.as_view()),
    path('properties/', PropertyList.as_view()),
    path('propertycreate/', PropertyCreate.as_view()),
    path('property/<int:pk>', PropertytDetail.as_view()),
]
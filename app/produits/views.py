from rest_framework import generics
from .models import Produit, Category, SubCategory, ProductAttribute,Key
from .serializers import (
    ProduitDisplaySerializer, ProduitCreateUpdateSerializer,
    CategoryDisplaySerializer, CategoryCreateUpdateSerializer,
    SubCategoryDisplaySerializer, SubCategoryCreateUpdateSerializer,
    ProductAttributeDisplaySerializer, ProductAttributeCreateSerializer,
    KeyDisplaySerializer, KeyCreateSerializer
)

class ProduitListCreateView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProduitDisplaySerializer
        elif self.request.method == 'POST':
            return ProduitCreateUpdateSerializer

class ProduitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProduitDisplaySerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ProduitCreateUpdateSerializer

# Faites de même pour les vues de Category, SubCategory et ProductAttribute
# ...

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDisplaySerializer
        elif self.request.method == 'POST':
            return CategoryCreateUpdateSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryDisplaySerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return CategoryCreateUpdateSerializer

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubCategoryDisplaySerializer
        elif self.request.method == 'POST':
            return SubCategoryCreateUpdateSerializer

class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubCategoryDisplaySerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return SubCategoryCreateUpdateSerializer

class ProductAttributeListCreateView(generics.ListCreateAPIView):
    queryset = ProductAttribute.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductAttributeDisplaySerializer
        elif self.request.method == 'POST':
            return ProductAttributeCreateSerializer

class ProductAttributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductAttribute.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductAttributeDisplaySerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ProductAttributeCreateSerializer

class KeyListCreateView(generics.ListCreateAPIView):
    queryset = Key.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return KeyDisplaySerializer
        elif self.request.method == 'POST':
            return KeyCreateSerializer

class KeyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Key.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return KeyDisplaySerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return KeyCreateSerializer
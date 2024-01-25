# urls.py

from django.urls import path
from .views import (
    ProduitListCreateView, ProduitDetailView,
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
    ProductAttributeListCreateView, ProductAttributeDetailView,
        KeyListCreateView, KeyDetailView

)

urlpatterns = [
    path('produits/', ProduitListCreateView.as_view(), name='produit-list-create'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('attributes/', ProductAttributeListCreateView.as_view(), name='attribute-list-create'),
    path('attributes/<int:pk>/', ProductAttributeDetailView.as_view(), name='attribute-detail'),
    path('keys/', KeyListCreateView.as_view(), name='key-list-create'),
    path('keys/<int:pk>/', KeyDetailView.as_view(), name='key-detail'),
]

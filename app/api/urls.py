
from django.contrib import admin
from django.urls import path,include
from .views import CurrenTimeView, ShopAPIView

urlpatterns = [
    path('time/', CurrenTimeView.as_view()),
    path('', include('produits.urls'))
]

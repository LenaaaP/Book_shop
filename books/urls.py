from django.urls import path
from books.views import *

urlpatterns = [
    path('category/', home, name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]
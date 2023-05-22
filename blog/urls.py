from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogListView, name='blogs'),
    path('blogs/<int:_id>/', views.BlogDetailView, name='blog'),
]

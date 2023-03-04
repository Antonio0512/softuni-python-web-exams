from django.urls import path
from recipes_web import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('create/', views.create_page, name='page-create'),
    path('edit/<int:pk>/', views.edit_page, name='page-edit'),
    path('delete/<int:pk>/', views.delete_page, name='page-delete'),
    path('details/<int:pk>/', views.details_page, name='page-details'),
]
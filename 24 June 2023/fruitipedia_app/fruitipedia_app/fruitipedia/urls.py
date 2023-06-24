from django.urls import path

from fruitipedia_app.fruitipedia import views

urlpatterns = [
    path('', views.homepage, name='page-home'),
    path('dashboard/', views.dashboard, name='page-dashboard'),
    path('create/', views.create_fruit, name='fruit-create'),
    path('<int:pk>/details/', views.details_fruit, name='fruit-details'),
    path('<int:pk>/edit/', views.edit_fruit, name='fruit-edit'),
    path('<int:pk>/delete/', views.delete_fruit, name='fruit-delete'),
]
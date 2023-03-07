from django.urls import path, include

from plant import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('catalogue/', views.catalogue_page, name='page-catalogue'),
    path('create/', views.create_plant, name='plant-create'),
    path('details/<int:pk>/', views.details_plant, name='plant-details'),
    path('edit/<int:pk>/', views.edit_plant, name='plant-edit'),
    path('delete/<int:pk>/', views.delete_plant, name='plant-delete'),
    path('profile/', include([
        path('create/', views.create_profile, name='profile-create'),
        path('details/', views.details_profile, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ])),
]

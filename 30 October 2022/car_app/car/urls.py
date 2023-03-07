from django.urls import path, include

from car import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('catalogue/', views.catalogue_page, name='page-catalogue'),
    path('profile/', include([
        path('create/', views.create_profile, name='profile-create'),
        path('details/', views.details_profile, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ])),
    path('car/', include([
        path('create/', views.create_car, name='car-create'),
        path('<int:pk>/details/', views.details_car, name='car-details'),
        path('<int:pk>/edit/', views.edit_car, name='car-edit'),
        path('<int:pk>/delete/', views.delete_car, name='car-delete'),
    ]))
]
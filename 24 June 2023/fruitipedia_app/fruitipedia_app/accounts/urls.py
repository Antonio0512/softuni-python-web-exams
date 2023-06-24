from django.urls import path

from fruitipedia_app.accounts import views

urlpatterns = [
    path('create/', views.create_profile, name='profile-create'),
    path('details/', views.details_profile, name='profile-details'),
    path('edit', views.edit_profile, name='profile-edit'),
    path('delete/', views.delete_profile, name='profile-delete')
]

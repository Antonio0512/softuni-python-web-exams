from django.urls import path
from notes import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('add/', views.create_note_page, name='note-create'),
    path('edit/<int:pk>/', views.edit_note_page, name='note-edit'),
    path('delete/<int:pk>/', views.delete_note_page, name='note-delete'),
    path('details/<int:pk>/', views.details_note_page, name='note-details'),
    path('profile/', views.profile_page, name='page-profile'),
    path('profile-delete/', views.profile_delete, name='profile-delete'),
]
from django.urls import path, include

from games import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('dashboard/', views.dashboard_page, name='page-dashboard'),
    path('profile/', include([
        path('create/', views.create_profile, name='profile-create'),
        path('details/', views.details_profile, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ])),
    path('game/', include([
        path('create/', views.create_game, name='game-create'),
        path('details/<int:pk>/', views.details_game, name='game-details'),
        path('edit/<int:pk>/', views.edit_game, name='game-edit'),
        path('delete/<int:pk>/', views.delete_game, name='game-delete'),
    ]))
]
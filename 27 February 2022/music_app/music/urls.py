from django.urls import path, include

from music import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('album/', include([
        path('add/', views.add_album, name='album-add'),
        path('details/<int:pk>/', views.details_album, name='album-details'),
        path('edit/<int:pk>/', views.edit_album, name='album-edit'),
        path('delete/<int:pk>/', views.delete_album, name='album-delete'),
    ])),
    path('profile/', include([
        path('details/', views.details_profile, name='profile-details'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ]))
]
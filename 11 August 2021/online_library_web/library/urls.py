from django.urls import path, include

from library import views

urlpatterns = [
    path('', views.home_page, name='page-home'),
    path('add/', views.book_add_page, name='book-add'),
    path('edit/<int:pk>/', views.book_edit_page, name='book-edit'),
    path('delete/<int:pk>/', views.book_delete_page, name='book-delete'),
    path('details/<int:pk>/', views.book_details_page, name='book-details'),
    path('profile/', include([
        path('', views.profile_page, name='page-profile'),
        path('edit/', views.profile_edit_page, name='profile-edit'),
        path('delete/', views.profile_delete_page, name='profile-delete'),
    ])),

]
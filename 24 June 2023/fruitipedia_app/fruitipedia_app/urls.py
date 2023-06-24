from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('fruitipedia_app.accounts.urls')),
    path('', include('fruitipedia_app.fruitipedia.urls'))
]

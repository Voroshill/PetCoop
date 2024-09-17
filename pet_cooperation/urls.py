from django.contrib import admin
from django.urls import path, include
from search_site.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search_site.urls')),
]

handler404 = page_not_found

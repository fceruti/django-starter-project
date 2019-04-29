from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.misc.hello_universe_urls')),
    path('admin/', admin.site.urls),
]

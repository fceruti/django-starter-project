from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path('', include('apps.misc.hello_universe_urls')),
    path('admin/', admin.site.urls),
]

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)), )

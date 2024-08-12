from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Mine.views import index, visitor_count_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('', visitor_count_view, name='visitor_count'),
]


if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include('debug_toolbar.urls'))
    # ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
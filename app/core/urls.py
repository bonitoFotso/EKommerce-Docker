from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from upload.views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path('api/',include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]

from django.contrib import admin
from django.urls import path, include

from api.api_docs import docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + docs_urls

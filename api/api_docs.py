from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

api_project_description = """
Documentação da API para a gestão de comissões de uma organização de televendas.

Projeto final - Codenation - Aceleradev - Squad 4.

[Repositório](https://github.com/codenation-dev/squad-4-ad-python-2)
[Issues](https://github.com/codenation-dev/squad-4-ad-python-2/issues)

<a href="mailto:julioriffel@gmail.com" rel="noopener noreferrer" class="link">Contact Julio</a>
<a href="mailto:luanfsf@gmail.com" rel="noopener noreferrer" class="link">Contact Luan</a>
"""

schema_url_patterns = [path('api/', include('api.urls')), ]

schema_view = get_schema_view(
    openapi.Info(
        title="Televendas",
        default_version='v1',
        description=f"{api_project_description}",
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns
)

docs_urls = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

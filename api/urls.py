from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api.views import UserViewSet, PlanViewSet, SellerViewSet, SaleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'sales', SaleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('sellers/', views.sellers),
#     path('comissions/', views.comissions),
#     path('vendedores/<int:month>/', views.vendedores),  # todo <int:year>/<str:month>/
#     path('check_commision/', views.check_commision)
# ]

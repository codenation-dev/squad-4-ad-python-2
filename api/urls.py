from django.urls import include, path
from rest_framework import routers

from api.views.check_comission import check_comission_view
from api.views.monthly_comission import monthly_comission_view
from api.views.plan import PLanListView, PlanView
from api.views.sale import SaleListView, SaleView
from api.views.seller import SellerListView, SellerView
from api.views.user import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

user_urls = [
    # TODO Verificar se esta router com users é necessária na API
    path(r'', include(router.urls))
]

seller_urls = [
    path('sellers/', SellerListView.as_view(), name="sellers_list"),
    path('sellers/<int:pk>/', SellerView.as_view(), name="sellers"),
]

sales_urls = [
    path('sales/', SaleListView.as_view(), name="sales_list"),
    path('sales/<int:pk>/', SaleView.as_view(), name="sales"),
]

plan_urls = [
    path('plans/', PLanListView.as_view(), name="comission_plans_list"),
    path('plans/<int:pk>/', PlanView.as_view(), name="comission_plans"),
]

comission_functions_urls = [
    path('monthly_comission/<int:pk>/', monthly_comission_view, name="month_comission"),
    path('check_comission/', check_comission_view, name="check_comission"),
]

# URLPATTERNS is all of the above
urlpatterns = (
        user_urls +
        seller_urls +
        sales_urls +
        plan_urls +
        comission_functions_urls
)

# urlpatterns = [
#     path('sellers/', views.sellers),
#     path('comissions/', views.comissions),
#     path('vendedores/<int:month>/', views.vendedores),  # todo <int:year>/<str:month>/
#     path('check_commision/', views.check_commision)
# ]

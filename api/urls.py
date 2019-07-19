from django.urls import include, path
from rest_framework import routers

from api.views.seller import SellerListView, SellerView
from api.views.sale import SaleListView, SaleView
from api.views.plan import PLanListView, PlanView

from api.views.check_comission import check_comission_view
from api.views.month_comission import month_comission_view

from api.views.user import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

user_urls = [
    # TODO Verificar se esta model é necessária na API
    path(r'', include(router.urls))
]

seller_urls = [
    path('seller/', SellerListView.as_view(), name="seller_list"),
    path('seller/<int:pk>/', SellerView.as_view(), name="seller"),
]

sales_urls = [
    path('sale/', SaleListView.as_view(), name="sale_list"),
    path('sale/<int:pk>/', SaleView.as_view(), name="sale"),
]

plan_urls = [
    path('plan/', PLanListView.as_view(), name="comission_plan_list"),
    path('plan/<int:pk>/', PlanView.as_view(), name="comission_plan"),
]

comission_functions_urls = [
    path('month_comission/', month_comission_view, name="month_comission"),
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

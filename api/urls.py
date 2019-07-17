from django.urls import path

from . import views

urlpatterns = [
    path('sellers/', views.sellers),
    path('comissions/', views.comissions),
    path('vendedores/<int:month>/', views.vendedores),  # todo <int:year>/<str:month>/
    path('check_commision/', views.check_commision)
]

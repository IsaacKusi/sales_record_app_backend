
from django.urls import path
from . import views

from .views import MyTokenObtainPairView, saleItemSerializerView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getUser, name='getUser'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sale', saleItemSerializerView.as_view(), name='sale_item'),
]

from django.urls import path


from .views import MyTokenObtainPairView, SaleItemSerializerView, SaleItemsDelete, GetSalesSerializer

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sale', SaleItemSerializerView.as_view(), name='sale_item'),
    path('sale/<int:item_id>/<int:user_id>/', SaleItemsDelete.as_view(), name='delete_item'),
    path('sale/<int:user_id>/', GetSalesSerializer.as_view(), name='get_item'),
]
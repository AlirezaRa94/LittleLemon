from django.urls import path, include
from rest_framework.routers import DefaultRouter

from LittleLemonAPI import views


router = DefaultRouter()
router.register('menu-items', views.MenuItemViewSet)

app_name = 'LittleLemonAPI'

urlpatterns = [
	path('', include(router.urls)),
	path('groups/manager/users', views.Managers.as_view()),
	path('groups/manager/users/<int:pk>', views.ManagerDelete.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrews.as_view()),
	path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewDelete.as_view()),
    path('cart/menu-items', views.Cart.as_view()),
	path('orders', views.ListCreateOrders.as_view()),
]

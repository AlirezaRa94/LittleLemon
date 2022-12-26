from django.urls import path, include
from rest_framework.routers import DefaultRouter

from LittleLemonAPI import views


router = DefaultRouter()
router.register('menu-items', views.MenuItemViewSet)

app_name = 'LittleLemonAPI'

urlpatterns = [
	path('', include(router.urls)),
]


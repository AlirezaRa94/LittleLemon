from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS

from LittleLemonAPI.serializers import MenuItemSerializer
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.permissions import IsManagerOrReadOnly


class MenuItemViewSet(ModelViewSet):
    permission_classes = [IsManagerOrReadOnly]
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

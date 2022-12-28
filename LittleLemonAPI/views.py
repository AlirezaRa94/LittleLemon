from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from LittleLemonAPI import serializers, models
from LittleLemonAPI.permissions import IsManager, ReadOnly


class MenuItemViewSet(ModelViewSet):
    permission_classes = [IsManager|ReadOnly]
    serializer_class = serializers.MenuItemSerializer
    queryset = models.MenuItem.objects.all()


class Managers(generics.ListCreateAPIView):
    queryset = Group.objects.get(name='Manager').user_set.all()
    permission_classes = [IsManager]
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name='Manager')
            managers.user_set.add(user)
            return Response(
                {'message': f'{username} successfully added to managers group'},
                status.HTTP_201_CREATED
            )

        return Response(
            {'message': 'username is required'},
            status.HTTP_400_BAD_REQUEST
        )


class ManagerDelete(generics.DestroyAPIView):
    permission_classes = [IsManager]
    
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])
        managers = Group.objects.get(name='Manager')
        managers.user_set.remove(user)
        return Response(
            {'message': f'{user.username} successfully removed from managers group'},
            status.HTTP_200_OK
        )


class DeliveryCrews(generics.ListCreateAPIView):
    queryset = Group.objects.get(name='Delivery Crew').user_set.all()
    permission_classes = [IsManager]
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username:
            user = get_object_or_404(User, username=username)
            delivery_crews = Group.objects.get(name='Delivery Crew')
            delivery_crews.user_set.add(user)
            return Response(
                {'message': f'{username} successfully added to delivery crews group'},
                status.HTTP_201_CREATED
            )

        return Response(
            {'message': 'username is required'},
            status.HTTP_400_BAD_REQUEST
        )


class DeliveryCrewDelete(generics.DestroyAPIView):
    permission_classes = [IsManager]
    
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])
        delivery_crews = Group.objects.get(name='Delivery Crew')
        delivery_crews.user_set.remove(user)
        return Response(
            {'message': f'{user.username} successfully removed from delivery crews group'},
            status.HTTP_200_OK
        )


class Cart(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CartSerializer
    
    def get_queryset(self):
        return models.Cart.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        menuitem_id = serialized_data.validated_data['menuitem_id']
        quantity = serialized_data.validated_data['quantity']
        menuitem = models.MenuItem.objects.get(id=menuitem_id)
        serialized_data.validated_data['menuitem'] = menuitem
        serialized_data.validated_data['unit_price'] = menuitem.price
        serialized_data.validated_data['price'] = quantity * menuitem.price
        serialized_data.save(user=self.request.user)
        return Response(
            {'message': f'{menuitem.title} successfully added to the cart for {request.user.username}'},
            status.HTTP_201_CREATED
        )

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(
            {'message': f'Cart successfully emptied for {request.user.username}'},
            status.HTTP_200_OK
        )

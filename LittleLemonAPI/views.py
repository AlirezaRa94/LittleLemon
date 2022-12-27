from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response

from LittleLemonAPI.serializers import MenuItemSerializer, UserSerializer
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.permissions import IsManager, ReadOnly


class MenuItemViewSet(ModelViewSet):
    permission_classes = [IsManager|ReadOnly]
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class Managers(generics.ListCreateAPIView):
    queryset = Group.objects.get(name='Manager').user_set.all()
    permission_classes = [IsManager]
    serializer_class = UserSerializer

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
    serializer_class = UserSerializer

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

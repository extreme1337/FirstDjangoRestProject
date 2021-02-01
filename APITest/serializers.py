from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, CharityRegistration, UserRegistration, OrderedItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity', 'charity', 'category']


class CharityRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['email', 'charity_name', 'password', 'city']


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['email', 'username', 'charity_name', 'password', 'city']


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['email', 'password']


class CharityGetAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['email', 'charity_name', 'city']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ['item', 'order_date', 'item_name', 'quantity', 'username']

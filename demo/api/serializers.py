from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = ['task', 'completed', 'timestamp', 'updated', 'user']
from .models import entry
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class entrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = entry
        fields = '__all__'

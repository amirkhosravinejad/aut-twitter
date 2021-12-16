from rest_framework import serializers
from aut_twitter.models import api

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api
        fields = ('username', 'password')
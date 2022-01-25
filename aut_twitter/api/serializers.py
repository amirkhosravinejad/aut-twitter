from rest_framework import serializers
<<<<<<< HEAD
from aut_twitter.models import login_table

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = login_table
        fields = ('username')
=======
from aut_twitter.models import api

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api
        fields = ('username', 'password')
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493

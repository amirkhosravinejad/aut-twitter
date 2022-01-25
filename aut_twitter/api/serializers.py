from rest_framework import serializers
from aut_twitter.models import login_table

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = login_table
        fields = ('username')
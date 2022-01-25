from aut_twitter.models import login_table
from .serializers import UserSerializer
from rest_framework import serializers, viewsets


class userViewSet(viewsets.ModelViewSet):
    queryset = login_table.objects.all()
    serializer_class = UserSerializer
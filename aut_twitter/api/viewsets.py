from aut_twitter.models import api
from .serializers import UserSerializer
from rest_framework import serializers, viewsets


class userViewSet(viewsets.ModelViewSet):
    queryset = api.objects.all()
    serializer_class = UserSerializer
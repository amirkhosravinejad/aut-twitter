<<<<<<< HEAD
from aut_twitter.models import login_table
=======
from aut_twitter.models import api
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
from .serializers import UserSerializer
from rest_framework import serializers, viewsets


class userViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = login_table.objects.all()
=======
    queryset = api.objects.all()
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
    serializer_class = UserSerializer
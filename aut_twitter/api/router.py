from .viewsets import userViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', userViewSet)
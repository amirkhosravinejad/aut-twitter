from django.urls import include, path
from . import views
#from aut_twitter.views import UserViewSet
urlpatterns = [
    path('', views.show, name="home"),
    path('sign-up/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
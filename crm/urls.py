from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('/login', views.log_in, name="login"),
    path('/log_out', views.log_out, name="logout"),
    path('/register', views.register_user, name="register"),
]
from django.urls import path
from karbar.views import *

urlpatterns = [
    path("signup/" , SignUpView.as_view() , name = "signup"),
    path("login/"  , LoginView.as_view()  , name = "login"),
]

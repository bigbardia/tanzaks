from django.urls import path
from meme.views import *


urlpatterns = [
    path("" , MemeView.as_view() , name = "meme")
] 

from django.urls import path
from django.contrib.auth.views import LogoutView
from config.settings import LOGOUT_REDIRECT_URL
from .views import (
    signIn,
    signUp,
    logout
)

app_name = "accounts"


urlpatterns = [
    path("",signIn,name="signIn"),
    path("signUp/",signUp,name="signUp"),
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    
]
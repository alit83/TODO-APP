from django.urls import path
from .views import LoginView ,   SignupView

app_name = "account"


urlpatterns =[
    path('login/',LoginView,name='login-account'),
    path('signup/',SignupView,name='signup-account'),

]
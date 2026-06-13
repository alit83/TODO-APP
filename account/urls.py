from django.urls import path
from .views import LoginView ,   SignupView , LogOutView

app_name = "account"


urlpatterns =[
    path('login/',LoginView,name='login-account'),
    path('signup/',SignupView,name='signup-account'),
    path('logout/',LogOutView,name='logout-account')

]
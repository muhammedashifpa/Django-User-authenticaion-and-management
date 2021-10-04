from os import name
from django.urls import path
from . import views



app_name = 'shopping'
urlpatterns = [
    # path('',views.HomePageView.as_view(),name="home"),
    path('',views.passHome,name='passhome'),
    path('home/',views.home,name="home"),

    # path('login/',views.LoginPageView.as_view(),name='login'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    # path('register/',views.RegistrationView.as_view(),name='register'),
    path('register/',views.register,name='register')
]

from django.urls import include, path
from . import views

app_name='core'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('login', views.loginPage, name='login'),
]
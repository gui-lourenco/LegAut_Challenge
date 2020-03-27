from django.urls import include, path
from . import views

app_name='core'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user'),
    path('manager/', views.managerPage, name='manager'),
    path('create/', views.userCreatePage, name='userCreate'),
    path('settings/<str:user>', views.userSettingsPage, name='userSettings'),
    path('detail/<str:user>', views.userDetailPage, name='userDetail'),
    path('download/<str:file>', views.downloadPage, name='download'),
]
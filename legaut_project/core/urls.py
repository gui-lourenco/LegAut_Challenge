from django.urls import include, path
from . import views

app_name='core'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/<str:user>', views.userPage, name='user'),
    path('manager/', views.managerPage, name='manager'),
    path('create/', views.userCreatePage, name='userCreate'),
    path('createstep/<str:user>/<str:password>', views.clientCreatePage, name='clientCreate'),
    path('managersettings/<str:user>/<str:info>', views.managerSettingsPage, name='managerSettings'),
    path('usersettings/<str:user>/<str:info>', views.userSettingsPage, name='userSettings'),
    path('detail/<str:user>', views.userDetailPage, name='userDetail'),
    path('download/<str:file>', views.downloadPage, name='download'),
    path('delete/<str:user>/<str:file>', views.deleteContractPage, name='delete'),
    path('search/<str:user>/<str:key>', views.searchPage, name='search'),
]
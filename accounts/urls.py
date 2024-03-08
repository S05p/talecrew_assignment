from django.urls import path
from accounts import views

app_name='accounts'
urlpatterns = [
    path('join/',views.join,name='join'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/',views.user_info,name='user_info'),
]

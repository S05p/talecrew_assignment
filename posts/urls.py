from django.urls import path
from posts import views

app_name='posts'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.post,name='post'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.get_user, name='get_user'),
    path('user/all', views.get_users, name='get_users'),
    path('user/create', views.create_user, name='create_user'),
    path('user/<int:pk>', views.user_detail, name='user_detail'),
]
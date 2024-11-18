from django.urls import path
from . import views

urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('add-user-type/', views.add_user_type, name='add_user_type'),
    path('list-user-types/', views.list_user_types, name='list_user_types'),
    path('user-list/', views.user_list, name='user_list'),
    path('login/', views.user_login, name='login'),
    path('index/', views.index, name='index'),
    path('solicitudes/', views.solicitudes, name= 'solicitudes'),
]

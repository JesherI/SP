from django.urls import path
from .views import add_user, add_user_type, list_user_types, user_list, user_login, index

urlpatterns = [
    path('add-user/', add_user, name='add_user'),
    path('add-user-type/', add_user_type, name='add_user_type'),
    path('list-user-types/', list_user_types, name='list_user_types'),
    path('user-list/', user_list, name='user_list'),
    path('login/', user_login, name='login'),
    path('index/', index, name='index'),
]

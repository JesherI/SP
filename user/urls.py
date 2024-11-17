from django.urls import path
from .views import add_user, add_user_type, list_user_types

urlpatterns = [
    path('add-user/', add_user, name='add_user'),
    path('add-user-type/', add_user_type, name='add_user_type'),
    path('list-user-types/', list_user_types, name='list_user_types'),
]

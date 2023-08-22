from django.urls import path
from .views import login

urlpatterns = [
    # path('create/', createUser, name='createUser'),
    path('login/', login, name= 'login')
]

from django.urls import path
from .views import adminCreate , adminLogin
urlpatterns = [
    path('create/', adminCreate, name='admin_create'),
    path('login/', adminLogin, name= 'admin_login')
]

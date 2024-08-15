from django.urls import path, include
from .views import home, register
# from .views import login

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    # path('login/', login, name='login'),
    path('accounts/', include("allauth.urls")),
]
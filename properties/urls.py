from django.urls import path
from .views import stay_detail_info, listings, confirmation

app_name = 'properties'
urlpatterns = [
    path('', stay_detail_info, name='stay_detail_info'),
    path('listings/', listings, name='listings'),
    path('confirmation/', confirmation, name='confirmation')
]
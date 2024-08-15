from django.urls import path
from .views import selections, property_history

app_name = "tracking"

urlpatterns = [
    path("selections", selections, name='selections'),
    path("history/<int:prop_id>/", property_history, name='history')
]
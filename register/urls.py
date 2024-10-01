from django.urls import path
from .views import EntrepreneurCreateView

urlpatterns = [
    path('api/entrepreneurs/', EntrepreneurCreateView.as_view(), name='entrepreneur-create'),
]

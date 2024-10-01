from rest_framework import generics
from .models import Entrepreneur
from .serializers import EntrepreneurSerializer

class EntrepreneurCreateView(generics.CreateAPIView):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

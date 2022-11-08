from .models import Symbol
from rest_framework import viewsets, permissions
from .serializers import SymbolSerializer


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SymbolSerializer

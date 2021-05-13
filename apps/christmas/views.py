from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, filters
from .serializers import LetterSerializer
from .models import Letter

class LetterViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows letters to be viewed or edited.'''
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo', 'name']
    filterset_fields = ['created_at']
    # authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

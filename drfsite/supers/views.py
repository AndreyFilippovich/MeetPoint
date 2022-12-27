from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializers import CharactersSerializer
from .models import Character, Category
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination


class CharactersAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CharactersAPIList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CharactersAPIListPagination


class CharactersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsAuthenticated, )


class CharactersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsAdminOrReadOnly, )

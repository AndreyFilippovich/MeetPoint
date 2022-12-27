from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Character
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CharactersSerializer


class CharactersAPIListPagination(PageNumberPagination):
    '''Класс позволяет устанавливать пагинацию на конкретную функцию.
    page_size- количество страниц к показу;
    max_page_size- максимальное количество возможных страниц.
    '''
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CharactersAPIList(generics.ListCreateAPIView):
    '''Отвечает за показ контента пользователям.
    Если пользователь не авторизован, то может только смотреть.
    К классу применена отдельная пагинация вызванная в функции выше.
    '''
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CharactersAPIListPagination


class CharactersAPIUpdate(generics.RetrieveUpdateAPIView):
    '''Класс отвечает за редактирование постов.
    Редактировать могут только авторы публикации.
    '''
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CharactersAPIDestroy(generics.RetrieveDestroyAPIView):
    '''Класс отвечает за удаление контента.
    Эта функция доступна только администраторам.
    '''
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer
    permission_classes = (IsAdminOrReadOnly, )

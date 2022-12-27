from django.contrib import admin
from django.urls import include, path, re_path
from supers.views import (CharactersAPIDestroy, CharactersAPIList,
                          CharactersAPIUpdate)

urlpatterns = [
    # Отвечает за доступ к админке
    path('admin/', admin.site.urls),
    # Отвечает за вход/выход пользователей
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # Отвечает за показ контента
    path('api/v1/characters/', CharactersAPIList.as_view()),
    # Отвечает за рассмотрение постов по отдельности
    path('api/v1/characters/<int:pk>/', CharactersAPIUpdate.as_view()),
    # Отвечает за удаление постов
    path('api/v1/charactersdelete/<int:pk>/', CharactersAPIDestroy.as_view()),
    # Ведет на список всех пользователей
    path('api/v1/auth/', include('djoser.urls')),
    # Авторизация по токену
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

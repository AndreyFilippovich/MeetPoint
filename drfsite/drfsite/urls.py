from django.contrib import admin
from django.urls import path, include, re_path
from supers.views import *
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/characters/', CharactersAPIList.as_view()),
    path('api/v1/characters/<int:pk>/', CharactersAPIUpdate.as_view()),
    path('api/v1/charactersdelete/<int:pk>/', CharactersAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

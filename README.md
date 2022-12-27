# MeetPoint

### Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/) [![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

## Описание проекта

### Проект по подготовке бэкенда на базе Django REST Framework.

## Реализованные функции:

#### - Регистрация пользователей;
#### - Вход/выход пользователей (Аутентификация пользователя при помощи djoser);
#### - Просмотр, добавление, редактирование и удаление контента;
#### - Реализованы разные уровни доступа в зависимости от роли пользователя на сайте;
#### - Добавлена пагинация для более удобного просмотра контента.

## Запуск проекта:

#### Склонировать репозиторий:
> https://github.com/AndreyFilippovich/MeetPoint.git

#### Если ранее не пользовались, то скачать виртуальное окружение:
> pip install virtualenv

#### Установить виртуальное окружение:
> python -m venv venv

#### Активировать виртуальное окружение:
> source venv/scripts/activate

#### Установить зависимости командой:
> pip install -r requirements.txt

#### Перейти в директорию drfsite:
> cd drfsite

#### Создать миграции:
> python manage.py makemigrations

#### Применить миграции:
> python manage.py migrate

#### Создать суперпользователя:
> python manage.py createsuperuser

#### Далее запускаем сам проект:
> python manage.py runserver

## Проект будет доступен по адресу:
### http://127.0.0.1:8000/api/v1/

## Автор проекта
[AndreyFilippovich](https://github.com/AndreyFilippovich)  


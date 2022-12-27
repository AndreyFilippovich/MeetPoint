from django.contrib.auth.models import User
from django.db import models


class Character(models.Model):
    '''Это модель в которую будут записываться данные о персонажах.
    В title и content записываются имена и информация о персонажах.
    time_create, time_update и is_published
    отражают техническую информацию о публикациях.
    cat- это поле в котором указывается является персонаж злодеем или героем.
    user- это графа, в которой указывается автор публикации.
    '''
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='пользователь',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    '''Вспомогательная модель для модели Character.
    В поле name указывается злодей персонаж или герой.
    '''
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

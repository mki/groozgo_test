from django.db import models


class News(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

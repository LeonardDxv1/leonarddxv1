from django.db import models
from django.urls import reverse_lazy


class Textures(models.Model):
    title = models.CharField(max_length=158, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo = models.ImageField(upload_to='media/%y/%m/%d', verbose_name='Фото')
    external_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на скачивание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('view_texture', kwargs={'pk': self.pk})

    class Meta:
        verbose_name='Текстура'
        verbose_name_plural='Текстуры'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('categorytexture', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
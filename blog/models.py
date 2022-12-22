from django.db import models


class Employee(models.Model):
    img = models.ImageField(upload_to='photos/', verbose_name='Фото')
    name = models.CharField(max_length=25, verbose_name='Имя сотрудника')
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=12, verbose_name='Номер пользователя')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    img = models.ImageField(upload_to='photos/', verbose_name='Фото')
    text = models.CharField(max_length=100, verbose_name='Отзыв')

    def __str__(self):
        return self.text


class Spam(models.Model):
    email = models.EmailField()


import datetime
from django.db import models

from django.utils import timezone


class Acoount(models.Model):
    first_name = models.CharField("Ім\'я", max_length=50)
    last_name = models.CharField('Прізвище', max_length=50)
    username = models.CharField('Псевдонім', max_length=50)
    email = models.CharField('Електронна почта', max_length=16)
    password = models.CharField('Пароль', max_length=16)
    


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Акаунт'
        verbose_name_plural = 'Акаунти'
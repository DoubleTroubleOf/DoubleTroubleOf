import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Назва статті', max_length=100)
    article_text =  models.TextField('Текст статті')
    pub_date = models.DateTimeField('Дата публікації',auto_now=True)
    article_rate = models.FloatField('Рейтинг статті', default=0.0)

   
    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def calculate_rate(self, new_rate):
        if self.article_rate == 0.0:
            self.article_rate = float(new_rate)
        else:
            self.article_rate = (self.article_rate + float(new_rate)) / 2

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Ім*я автора', max_length=50)
    comment_text = models.CharField('Текст коментаря', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарій'
        verbose_name_plural = 'Коментарі'

class Indicator(models.Model):
    Kvartal = models.DecimalField('Квартал', max_digits= 1, decimal_places=0)
    Year = models.CharField('Рік', max_length=4)

    Income = models.DecimalField('Чистий дохід', max_digits= 5, decimal_places=0)
    
    
    def __str__(self):
        return str(self.Year)+':'+ str(self.Kvartal) + '  ||   ' + str(self.Income)

    class Meta:
        verbose_name = 'Показник ефективності'
        verbose_name_plural = 'Показники ефективності'

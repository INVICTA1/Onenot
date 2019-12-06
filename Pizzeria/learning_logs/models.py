from django.db import models


# Create your models here.
class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()  # create an unlimited text field

    date_added = models.DateTimeField(
        auto_now_add=True)  # select the records in the order they were created and mark each record with a timestamp
    class Meta:
        verbose_name_plural = 'entries'  # When referring to more than one entry we use the plural form entries
    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.text) < 50:
            return self.text[:50]
        else:
            return self.text[:50] + "..."

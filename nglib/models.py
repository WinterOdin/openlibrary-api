from django.db import models


class SearchStats(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    author_id = models.CharField(max_length=10)
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname} : {self.author_id}'
from django.db import models

from titles.models import Title


class Photo(models.Model):
    name = models.CharField(max_length=70)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

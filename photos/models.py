from django.db import models

from titles.models import Title


class Photo(models.Model):
    picture = models.ImageField(upload_to='gallery',blank=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, blank=True)


from django.db import models

from categories.models import Category


class Title(models.Model):
    """Defines Enrollment model"""

    title_name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_name

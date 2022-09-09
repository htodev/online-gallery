from django.db import models


class Category(models.Model):
    """Defines Enrollment model"""

    category_name = models.CharField(max_length=70)

    def __str__(self):
        return self.category_name
